export const THEME_PREFERENCES = Object.freeze(["system", "light", "dark"]);

const STORAGE_KEY = "jl-theme-preference";
const COOKIE_NAME = "jl_theme";

function normalizePreference(value) {
  return THEME_PREFERENCES.includes(value) ? value : "system";
}

function readCookie(document) {
  const match = document.cookie.match(new RegExp(`(?:^|; )${COOKIE_NAME}=([^;]*)`));
  return match ? normalizePreference(decodeURIComponent(match[1])) : null;
}

function readPreference(window) {
  const cookie = readCookie(window.document);
  if (cookie) return cookie;
  try {
    return normalizePreference(window.localStorage.getItem(STORAGE_KEY));
  } catch {
    return "system";
  }
}

function writePreference(window, preference) {
  const secure = window.location.protocol === "https:" ? "; Secure" : "";
  const domain = window.location.hostname.endsWith("johnnyli.dev") ? "; Domain=.johnnyli.dev" : "";
  window.document.cookie = `${COOKIE_NAME}=${encodeURIComponent(preference)}; Path=/; Max-Age=31536000; SameSite=Lax${domain}${secure}`;
  try {
    window.localStorage.setItem(STORAGE_KEY, preference);
  } catch {
    // Cookie persistence remains available when storage is blocked.
  }
}

function resolveTheme(window, preference) {
  return preference === "dark"
    || (preference === "system" && window.matchMedia("(prefers-color-scheme: dark)").matches)
    ? "dark"
    : "light";
}

export function applyTheme(preference, targetWindow = window) {
  const normalized = normalizePreference(preference);
  const theme = resolveTheme(targetWindow, normalized);
  const root = targetWindow.document.documentElement;
  root.dataset.themePreference = normalized;
  root.dataset.theme = theme;
  root.dispatchEvent(new CustomEvent("jl-theme-change", {
    bubbles: false,
    detail: { preference: normalized, theme },
  }));
  return { preference: normalized, theme };
}

export function installThemeController(targetWindow = window) {
  let preference = readPreference(targetWindow);
  const media = targetWindow.matchMedia("(prefers-color-scheme: dark)");
  const listeners = new Set();

  const notify = () => {
    const state = applyTheme(preference, targetWindow);
    for (const listener of listeners) listener(state);
    return state;
  };

  const handleSystemChange = () => {
    if (preference === "system") notify();
  };
  media.addEventListener("change", handleSystemChange);
  let state = notify();

  return {
    getState() {
      return state;
    },
    setPreference(nextPreference) {
      preference = normalizePreference(nextPreference);
      writePreference(targetWindow, preference);
      state = notify();
      return state;
    },
    subscribe(listener) {
      listeners.add(listener);
      listener(state);
      return () => listeners.delete(listener);
    },
    destroy() {
      media.removeEventListener("change", handleSystemChange);
      listeners.clear();
    },
  };
}

export function installThemePicker(root, controller = installThemeController(root.ownerDocument.defaultView)) {
  if (!(root instanceof HTMLElement)) throw new TypeError("Theme picker root must be an HTMLElement.");
  const buttons = [...root.querySelectorAll("[data-theme-option]")];
  const update = ({ preference }) => {
    for (const button of buttons) {
      const selected = button.getAttribute("data-theme-option") === preference;
      button.setAttribute("aria-pressed", String(selected));
      button.classList.toggle("jl-theme-option--selected", selected);
    }
  };
  const unsubscribe = controller.subscribe(update);
  const handleClick = (event) => {
    const button = event.target instanceof Element ? event.target.closest("[data-theme-option]") : null;
    if (!(button instanceof HTMLButtonElement)) return;
    controller.setPreference(button.getAttribute("data-theme-option"));
  };
  root.addEventListener("click", handleClick);
  return {
    controller,
    destroy() {
      unsubscribe();
      root.removeEventListener("click", handleClick);
    },
  };
}
