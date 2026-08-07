const fs = require('node:fs');
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const report = [];
  fs.mkdirSync('candidate-visual', { recursive: true });

  for (const theme of ['light', 'dark']) {
    for (const [name, viewport] of [
      ['desktop', { width: 1440, height: 900 }],
      ['mobile', { width: 390, height: 844 }],
      ['minimum', { width: 320, height: 700 }],
    ]) {
      const context = await browser.newContext({
        viewport,
        deviceScaleFactor: 2,
        colorScheme: theme,
        reducedMotion: 'reduce',
      });
      await context.addInitScript((value) => localStorage.setItem('jl-theme', value), theme);
      const page = await context.newPage();
      await page.goto('http://127.0.0.1:4173/', { waitUntil: 'networkidle' });
      const button = page.locator('.jl-site-switcher__button');
      const menu = page.locator('[data-site-switcher-menu]');
      await button.click();
      await menu.waitFor({ state: 'visible' });
      await page.screenshot({ path: `candidate-visual/sites-open-${name}-${theme}.png`, fullPage: false });
      await page.locator('.jl-site-switcher').screenshot({ path: `candidate-visual/sites-control-${name}-${theme}.png` });

      const metrics = await page.evaluate(() => {
        const button = document.querySelector('.jl-site-switcher__button');
        const menu = document.querySelector('[data-site-switcher-menu]');
        const links = [...document.querySelectorAll('[data-site-switcher-menu] a')];
        const rootStyle = getComputedStyle(document.documentElement);
        const rect = (el) => {
          const r = el.getBoundingClientRect();
          return { left: r.left, right: r.right, top: r.top, bottom: r.bottom, width: r.width, height: r.height };
        };
        const mr = rect(menu);
        return {
          viewportWidth: innerWidth,
          documentWidth: document.documentElement.scrollWidth,
          button: rect(button),
          menu: mr,
          buttonBorderColor: getComputedStyle(button).borderTopColor,
          accentColor: rootStyle.getPropertyValue('--jl-color-accent').trim(),
          links: links.map((el) => ({
            text: el.textContent.trim(),
            rect: rect(el),
            scrollWidth: el.scrollWidth,
            clientWidth: el.clientWidth,
          })),
          rowOverflow: links.some((el) => {
            const r = el.getBoundingClientRect();
            return r.left < mr.left - 0.5 || r.right > mr.right + 0.5;
          }),
        };
      });

      report.push({ theme, name, ...metrics });
      if (Math.abs(metrics.button.width - 88) > 0.75) throw new Error(`${theme}/${name}: Sites trigger width ${metrics.button.width}`);
      if (Math.abs(metrics.menu.width - 144) > 0.75) throw new Error(`${theme}/${name}: Sites menu width ${metrics.menu.width}`);
      if (metrics.menu.left < -0.5 || metrics.menu.right > metrics.viewportWidth + 0.5) throw new Error(`${theme}/${name}: menu outside viewport ${metrics.menu.left}/${metrics.menu.right}`);
      if (metrics.rowOverflow) throw new Error(`${theme}/${name}: menu row escaped dropdown bounds`);
      if (metrics.links.some((link) => link.scrollWidth > link.clientWidth + 1)) throw new Error(`${theme}/${name}: menu text clips`);
      if (metrics.documentWidth > metrics.viewportWidth + 1) throw new Error(`${theme}/${name}: horizontal overflow ${metrics.documentWidth}/${metrics.viewportWidth}`);
      if (metrics.buttonBorderColor === metrics.accentColor) throw new Error(`${theme}/${name}: expanded pointer hover still uses accent border`);
      await context.close();
    }
  }

  fs.writeFileSync('candidate-visual/report.json', JSON.stringify(report, null, 2));
  await browser.close();
})();
