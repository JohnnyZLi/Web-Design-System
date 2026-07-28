const TIMEOUT_MS = 20_000;
const OWNED_LINKS = [
  "https://johnnyli.dev",
  "https://network.johnnyli.dev",
  "https://rolepacket.johnnyli.dev",
];

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

async function request(url, options = {}) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), TIMEOUT_MS);
  try {
    return await fetch(url, {
      cache: "no-store",
      signal: controller.signal,
      ...options,
      headers: {
        "user-agent": "Johnny-Li-Web-Design-System-Smoke/1.0",
        ...(options.headers ?? {}),
      },
    });
  } finally {
    clearTimeout(timeout);
  }
}

async function checkPublicSite({ name, url, marker }) {
  const response = await request(url, { redirect: "follow" });
  assert(response.ok, `${name} returned HTTP ${response.status}.`);
  const html = await response.text();
  assert(html.includes(marker), `${name} is missing its expected product marker.`);
  assert(html.includes("jl-global-header"), `${name} is missing the shared global header.`);
  for (const ownedLink of OWNED_LINKS) {
    assert(html.includes(ownedLink), `${name} is missing owned-site link ${ownedLink}.`);
  }
  return { name, status: response.status, finalUrl: response.url, mode: "public" };
}

async function checkRolePacket() {
  const clientId = process.env.ROLEPACKET_ACCESS_CLIENT_ID;
  const clientSecret = process.env.ROLEPACKET_ACCESS_CLIENT_SECRET;
  const authenticated = Boolean(clientId && clientSecret);
  const response = await request("https://rolepacket.johnnyli.dev", {
    redirect: authenticated ? "follow" : "manual",
    headers: authenticated
      ? {
          "CF-Access-Client-Id": clientId,
          "CF-Access-Client-Secret": clientSecret,
        }
      : {},
  });

  if (authenticated) {
    assert(response.ok, `RolePacket authenticated smoke returned HTTP ${response.status}.`);
    const html = await response.text();
    assert(html.includes("RolePacket"), "RolePacket authenticated smoke is missing the app marker.");
    assert(html.includes("jl-global-header"), "RolePacket authenticated smoke is missing the shared header.");
    for (const ownedLink of OWNED_LINKS) {
      assert(html.includes(ownedLink), `RolePacket is missing owned-site link ${ownedLink}.`);
    }
    return { name: "RolePacket", status: response.status, finalUrl: response.url, mode: "authenticated" };
  }

  const location = response.headers.get("location") ?? "";
  const protectedResponse = response.status === 302 || response.status === 303 || response.status === 307 || response.status === 308;
  assert(protectedResponse, `RolePacket unauthenticated smoke expected an Access redirect, received HTTP ${response.status}.`);
  assert(
    location.includes("cloudflareaccess.com") || location.includes("/cdn-cgi/access"),
    "RolePacket redirected somewhere other than Cloudflare Access.",
  );
  return { name: "RolePacket", status: response.status, finalUrl: location, mode: "access-gate" };
}

const checks = await Promise.all([
  checkPublicSite({ name: "Portfolio", url: "https://johnnyli.dev", marker: "Johnny Li" }),
  checkPublicSite({ name: "Network Diagnostics", url: "https://network.johnnyli.dev", marker: "Network Diagnostics" }),
  checkRolePacket(),
]);

for (const check of checks) {
  console.log(`${check.name}: HTTP ${check.status} (${check.mode}) ${check.finalUrl}`);
}
console.log("Deployed-site smoke checks passed.");