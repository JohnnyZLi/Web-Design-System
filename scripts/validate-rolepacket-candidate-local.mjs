#!/usr/bin/env node
import { mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const scriptRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const npm = process.platform === "win32" ? "npm.cmd" : "npm";

function parseArguments(argv) {
  const options = { rolepacket: null };
  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument !== "--rolepacket") throw new Error(`Unknown argument: ${argument}`);
    const value = argv[index + 1];
    if (!value || value.startsWith("--")) throw new Error("--rolepacket requires a repository path.");
    options.rolepacket = resolve(value);
    index += 1;
  }
  if (!options.rolepacket) throw new Error("Pass the local RolePacket repository with --rolepacket <path>.");
  return options;
}

function run(command, args, cwd, options = {}) {
  console.log(`\n> (${cwd}) ${command} ${args.join(" ")}`);
  const result = spawnSync(command, args, {
    cwd,
    env: { ...process.env, ...options.env },
    encoding: options.capture ? "utf8" : undefined,
    stdio: options.capture ? ["ignore", "pipe", "pipe"] : "inherit",
  });
  if (result.error) throw result.error;
  if (result.status !== 0) {
    const detail = options.capture ? `\n${result.stderr || result.stdout || ""}` : "";
    throw new Error(`${command} ${args.join(" ")} exited with status ${result.status}.${detail}`);
  }
  return options.capture ? String(result.stdout).trim() : "";
}

function capture(command, args, cwd) {
  return run(command, args, cwd, { capture: true });
}

async function main() {
  const options = parseArguments(process.argv.slice(2));
  const candidateVersion = String(JSON.parse(await readFile(resolve(scriptRoot, "version.json"), "utf8")).version ?? "");
  const candidateSha = capture("git", ["rev-parse", "HEAD"], scriptRoot);

  if (!/^\d+\.\d+\.\d+$/.test(candidateVersion)) throw new Error(`Invalid candidate version: ${candidateVersion}`);
  if (!/^[0-9a-f]{40}$/.test(candidateSha)) throw new Error(`Invalid candidate commit: ${candidateSha}`);

  capture("git", ["rev-parse", "--show-toplevel"], options.rolepacket);
  run("git", ["fetch", "origin", "main"], options.rolepacket);
  const rolepacketSha = capture("git", ["rev-parse", "origin/main"], options.rolepacket);
  if (!/^[0-9a-f]{40}$/.test(rolepacketSha)) throw new Error(`Invalid RolePacket main commit: ${rolepacketSha}`);

  const temporaryRoot = await mkdtemp(join(tmpdir(), "rolepacket-wds-candidate-"));
  const worktree = resolve(temporaryRoot, "consumer");
  let worktreeCreated = false;

  try {
    run("git", ["worktree", "add", "--detach", worktree, rolepacketSha], options.rolepacket);
    worktreeCreated = true;

    await writeFile(
      resolve(worktree, "design-system.lock.json"),
      `${JSON.stringify({ package: "@johnnyzli/web-design-system", version: candidateVersion, sourceCommit: candidateSha }, null, 2)}\n`,
      "utf8",
    );
    await writeFile(
      resolve(worktree, "src/client/design-system/SOURCE.md"),
      [
        "# Generated design-system assets",
        "",
        "Do not edit these files directly.",
        "",
        "Package: @johnnyzli/web-design-system",
        `Version: ${candidateVersion}`,
        `Source commit: ${candidateSha}`,
        "",
        "Validate with `npm run design-system:check`.",
        "",
      ].join("\n"),
      "utf8",
    );

    run(npm, ["ci", "--no-audit", "--no-fund"], worktree, {
      env: { PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD: "1" },
    });
    run(npm, ["run", "design-system:sync"], worktree);
    run(npm, ["run", "verify:local:quick"], worktree);
    run(npm, ["audit", "--omit=dev", "--audit-level=high"], worktree);

    const synchronizedVersion = String(
      JSON.parse(await readFile(resolve(worktree, "src/client/design-system/version.json"), "utf8")).version ?? "",
    );
    if (synchronizedVersion !== candidateVersion) {
      throw new Error(`Synchronized RolePacket version ${synchronizedVersion} does not match candidate ${candidateVersion}.`);
    }

    console.log("\nLOCAL_ROLEPACKET_CANDIDATE_PASS");
    console.log(`Design system: ${candidateVersion} @ ${candidateSha}`);
    console.log(`RolePacket main: ${rolepacketSha}`);
  } finally {
    if (worktreeCreated) {
      spawnSync("git", ["worktree", "remove", "--force", worktree], {
        cwd: options.rolepacket,
        stdio: "inherit",
      });
    }
    await rm(temporaryRoot, { recursive: true, force: true });
  }
}

main().catch((error) => {
  console.error(`Local RolePacket candidate validation failed: ${error instanceof Error ? error.message : String(error)}`);
  process.exitCode = 1;
});
