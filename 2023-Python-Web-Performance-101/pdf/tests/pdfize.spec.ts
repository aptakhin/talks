import { test, expect } from '@playwright/test';


test('screenshot', async ({ page }) => {
  await page.goto('http://localhost:4004/2023-Python-Web-Performance-101/')
  await new Promise(f => setTimeout(f, 1000));
  // await expect(page.locator("py-splashscreen")).toHaveCount(0)
  await page.locator("py-splashscreen").isHidden();
  await new Promise(f => setTimeout(f, 1000));

  // await page.pdf({ path: 'page1.pdf' });


  let pageNumber = 1

  while (1) {
    const pageFilenumber = pageNumber.toString().padStart(2, '0')

    await page.locator(".pres-scene--choosen").press('KeyD')
    await new Promise(f => setTimeout(f, 200))

    await page.pdf({ path: 'out/page' + pageFilenumber + '.pdf' })
    pageNumber += 1

    const visiblePyTerminals = await page.$$("py-terminal:visible");
    console.log('DD', pageNumber, 'pyterm', visiblePyTerminals.length)

    if (visiblePyTerminals.length) {
      const visiblePyTerminal = await page.locator("py-terminal:visible")
      await visiblePyTerminal.press('Shift+Enter')
      await new Promise(f => setTimeout(f, 3000))
      await page.pdf({ path: 'out/page' + pageFilenumber + '.pdf' })
      pageNumber += 1
    }

    const lastMark = await page.$("islast:visible");
    if (lastMark !== null) {
      break
    }
  }
});
