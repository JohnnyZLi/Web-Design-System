(() => {
  const root = document.documentElement;
  const storageKey = "jl-theme-preference";
  const cookieName = "jl_theme";
  const allowed = new Set(["system", "light", "dark"]);

  const cookieMatch = document.cookie.match(new RegExp(`(?:^|; )${cookieName}=([^;]*)`));
  let preference = cookieMatch ? decodeURIComponent(cookieMatch[1]) : "";
  if (!allowed.has(preference)) {
    try {
      preference = window.localStorage.getItem(storageKey) || "system";
    } catch {
      preference = "system";
    }
  }
  if (!allowed.has(preference)) preference = "system";

  const dark = preference === "dark"
    || (preference === "system" && window.matchMedia("(prefers-color-scheme: dark)").matches);

  root.dataset.themePreference = preference;
  root.dataset.theme = dark ? "dark" : "light";
})();
