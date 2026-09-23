import asyncio
from playwright.async_api import async_playwright

SITE_URL = "https://koalafaucet.com/doge-claim"
EMAILS = [
    "Omidsaadatsafai2012@gmail.com",
    "Omidsaadatsafai2003@gmail.com",
    "Omidsaadatsafai2001@gmail.com",
]

async def do_email(browser, email):
    context = await browser.new_context()
    page = await context.new_page()

    print(f"→ ایمیل: {email}")
    await page.goto(SITE_URL, wait_until="domcontentloaded")

    await page.click("button")
    await asyncio.sleep(3)

    await page.fill("input", email)
    await asyncio.sleep(2)

    await page.click("button")
    print(f"✔ {email} انجام شد")

    await context.close()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        await asyncio.gather(*[do_email(browser, e) for e in EMAILS])
        await browser.close()

asyncio.run(main())
