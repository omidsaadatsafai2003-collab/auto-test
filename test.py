import asyncio
from playwright.async_api import async_playwright

SITE_URL = "https://koalafaucet.com/doge"
EMAILS = [
    "omidsaadatsafai2012@gmail.com",
]

WAIT_AFTER_FIRST_CLICK = 17   # چند ثانیه صبر بعد از CLAIM FREE DOGE
WAIT_AFTER_SECOND_CLICK = 3   # چند ثانیه صبر بعد از CLAIM NOW

async def do_email(browser, email):
    context = await browser.new_context()
    page = await context.new_page()

    print(f"→ ایمیل: {email}")
    await page.goto(SITE_URL, wait_until="domcontentloaded")

    # ۱. کلیک روی CLAIM FREE DOGE
    print("   کلیک روی CLAIM FREE DOGE...")
    await page.click("text=CLAIM FREE DOGE")
    await asyncio.sleep(WAIT_AFTER_FIRST_CLICK)

    # ۲. کلیک روی CLAIM NOW (بعد از تایمر)
    print("   کلیک روی CLAIM NOW...")
    await page.click("text=CLAIM NOW", timeout=30000)
    await asyncio.sleep(WAIT_AFTER_SECOND_CLICK)

    # ۳. وارد کردن ایمیل
    print(f"   وارد کردن ایمیل: {email}")
    await page.fill("input[type='email']", email)
    await asyncio.sleep(1)

    # ۴. کلیک روی Send DOGE
    print("   کلیک روی Send DOGE...")
    await page.click("text=Send DOGE")
    await asyncio.sleep(3)

    print(f"✔ {email} — انجام شد")
    await context.close()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        await asyncio.gather(*[do_email(browser, e) for e in EMAILS])
        await browser.close()

asyncio.run(main())
