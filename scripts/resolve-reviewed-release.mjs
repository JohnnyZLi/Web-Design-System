import { mkdir, readFile, writeFile } from "node:fs/promises";
import { dirname, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const REPOSITORY = "JohnnyZLi/Web-Design-System";
const PACKAGE = "@johnnyzli/web-design-system";
const APPROVED_STATUS = "approved";
const SHA = /^[0-9a-f]{40}$/;
const VERSION = /^\d+\.\d+\.\d+$/;
const RETRYABLE_STATUS = new Set([408, 425, 429, 500, 502, 503, 504]);
const HISTORY_PAGE_SIZE = 100;
const MAX_HISTORY_PAGES = 5;
const DEFAULT_MAX_ATTEMPTS = 4;
const DEFAULT_BASE_DELAY_MS = 250;
const DEFAULT_MAX_DELAY_MS = 4000;

function localPath(value) {
  const root = resolve(".");
  const destination = resolve(String(value));
  const relation = relative(root, destination);
  if (!relation || relation.startsWith("..") || relation.includes("../")) {
    throw new Error(`Consumer path must stay inside the repository: ${value}`);
  }
  return destination;
}

async function json(path) {
  return JSON.parse(await readFile(localPath(path), "utf8"));
}

async function writeJson(path, value) {
  const destination = localPath(path);
  await mkdir(dirname(destination), { recursive: true });
  await writeFile(destination, `${JSON.stringify(value, null, 2)}\n`, "utf8");
}

function retryAfterMilliseconds(response) {
  const value = response.headers?.get?.("retry-after");
  if (!value) return null;
  if (/^\d+(?:\.\d+)?$/.test(value)) return Math.max(0, Number(value) * 1000);
  const when = Date.parse(value);
  return Number.isFinite(when) ? Math.max(0, when - Date.now()) : null;
}

function isRetryableResponse(response) {
  const status = Number(response.status);
  if (RETRYABLE_STATUS.has(status) || status >= 500) return true;
  if (status !== 403) return false;
  const retryAfter = response.headers?.get?.("retry-after");
  const remaining = response.headers?.get?.("x-ratelimit-remaining");
  return Boolean(retryAfter) || remaining === "0";
}

function retryDelay(response, attempt, baseDelayMs, maxDelayMs) {
  const requested = retryAfterMilliseconds(response);
  if (requested !== null) return Math.min(requested, maxDelayMs);
  return Math.min(baseDelayMs * (2 ** (attempt - 1)), maxDelayMs);
}

async function defaultSleep(milliseconds) {
  await new Promise((resolvePromise) => setTimeout(resolvePromise, milliseconds));
}

export async function requestWithRetry(
  url,
  accept = "application/vnd.github+json",
  {
    fetchImpl = globalThis.fetch,
    sleepImpl = defaultSleep,
    maxAttempts = DEFAULT_MAX_ATTEMPTS,
    baseDelayMs = DEFAULT_BASE_DELAY_MS,
    maxDelayMs = DEFAULT_MAX_DELAY_MS,
    token = process.env.GITHUB_TOKEN ?? "",
  } = {},
) {
  if (typeof fetchImpl !== "function") throw new Error("A fetch implementation is required.");
  let lastNetworkError = null;

  for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
    let response;
    try {
      const headers = {
        accept,
        "user-agent": "Johnny-Li-Design-System-Consumer/2.0",
      };
      if (token && String(url).startsWith("https://api.github.com/")) {
        headers.authorization = `Bearer ${token}`;
        headers["x-github-api-version"] = "2022-11-28";
      }
      response = await fetchImpl(url, { headers });
    } catch (error) {
      lastNetworkError = error;
      if (attempt === maxAttempts) {
        throw new Error(
          `Design-system request failed after ${maxAttempts} attempts: network error: ${error?.message ?? error}`,
          { cause: error },
        );
      }
      await sleepImpl(Math.min(baseDelayMs * (2 ** (attempt - 1)), maxDelayMs));
      continue;
    }

    if (response.ok) return response;

    const status = Number(response.status);
    const retryable = isRetryableResponse(response);
    if (!retryable || attempt === maxAttempts) {
      throw new Error(
        `Design-system request failed: ${status} ${response.statusText || "HTTP error"}`
        + (retryable ? ` after ${attempt} attempts` : ""),
      );
    }

    await sleepImpl(retryDelay(response, attempt, baseDelayMs, maxDelayMs));
  }

  throw new Error(`Design-system request failed: ${lastNetworkError?.message ?? "unknown network error"}`);
}

function validateMetadata(metadata, sourceCommit) {
  const name = String(metadata?.name ?? "");
  const version = String(metadata?.version ?? "");
  const status = String(metadata?.status ?? "");
  if (name !== PACKAGE) throw new Error(`Design system ${sourceCommit} returned an unexpected package name.`);
  if (!VERSION.test(version)) throw new Error(`Design system ${sourceCommit} returned an invalid semantic version.`);
  return { name, version, status };
}

async function metadataAt(sourceCommit, requestOptions) {
  const response = await requestWithRetry(
    `https://raw.githubusercontent.com/${REPOSITORY}/${sourceCommit}/version.json`,
    "application/json",
    requestOptions,
  );
  return validateMetadata(await response.json(), sourceCommit);
}

export async function resolveLatestApprovedRelease({ requestOptions = {} } = {}) {
  let targetVersion = null;
  let approvedRelease = null;

  for (let page = 1; page <= MAX_HISTORY_PAGES; page += 1) {
    const response = await requestWithRetry(
      `https://api.github.com/repos/${REPOSITORY}/commits?path=version.json&per_page=${HISTORY_PAGE_SIZE}&page=${page}`,
      "application/vnd.github+json",
      requestOptions,
    );
    const commits = await response.json();
    if (!Array.isArray(commits)) throw new Error("Design system returned invalid version history.");

    for (const commit of commits) {
      const sourceCommit = String(commit?.sha ?? "");
      if (!SHA.test(sourceCommit)) throw new Error("Design system returned an invalid commit SHA.");
      const metadata = await metadataAt(sourceCommit, requestOptions);

      if (targetVersion === null) {
        if (metadata.status !== APPROVED_STATUS) continue;
        targetVersion = metadata.version;
        approvedRelease = { package: PACKAGE, version: metadata.version, sourceCommit };
        continue;
      }

      if (metadata.version !== targetVersion || metadata.status !== APPROVED_STATUS) {
        return approvedRelease;
      }

      // Walk backwards through metadata-only edits that left the same release
      // approved. The oldest commit in this contiguous approved epoch is the
      // immutable approval boundary consumers should pin.
      approvedRelease = { package: PACKAGE, version: metadata.version, sourceCommit };
    }

    if (commits.length < HISTORY_PAGE_SIZE) break;
  }

  if (!approvedRelease) throw new Error("Design system has no approved release in version history.");
  return approvedRelease;
}

export async function updateConsumerRelease({
  lockFile = "design-system.lock.json",
  packageJson = null,
  requestOptions = {},
} = {}) {
  const release = await resolveLatestApprovedRelease({ requestOptions });
  await writeJson(lockFile, release);

  if (packageJson) {
    const manifest = await json(packageJson);
    manifest.dependencies ??= {};
    manifest.dependencies[PACKAGE] = `github:${REPOSITORY}#${release.sourceCommit}`;
    await writeJson(packageJson, manifest);
  }

  return release;
}

function parseArguments(argv) {
  const options = { lockFile: "design-system.lock.json", packageJson: null };
  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument === "--lock") options.lockFile = argv[++index];
    else if (argument === "--package-json") options.packageJson = argv[++index];
    else throw new Error(`Unknown argument: ${argument}`);
    if (!argv[index]) throw new Error(`Missing value for ${argument}`);
  }
  return options;
}

const invokedPath = process.argv[1] ? resolve(process.argv[1]) : null;
if (invokedPath === fileURLToPath(import.meta.url)) {
  try {
    const release = await updateConsumerRelease(parseArguments(process.argv.slice(2)));
    console.log(`Locked ${release.package} v${release.version} at approved commit ${release.sourceCommit}.`);
  } catch (error) {
    console.error(`Error: ${error?.message ?? error}`);
    process.exitCode = 1;
  }
}
