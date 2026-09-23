import asyncio
from playwright.async_api import async_playwright

SITE_URL = "https://koalafaucet.com/doge"
EMAILS = [
    "omidsaadatsafai2012@gmail.com",
]

async def do_email(browser, email):
    context = await browser.new_context(
        user_agent="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    )
    page = await context.new_page()

    print(f"→ ایمیل: {email}")
    await page.goto(SITE_URL, wait_until="domcontentloaded")
    await asyncio.sleep(5)

    # عکس از صفحه بگیر
    await page.screenshot(path="debug.png", full_page=True)
    print("   عکس صفحه گرفته شد → debug.png")

    # محتوای صفحه رو چاپ کن
    content = await page.content()
    print("   طول محتوا:", len(content))
    print("   بخش اول محتوا:", content[:500])

    # ببین دکمه‌ها چی هستن
    buttons = await page.locator("button").all()
    print(f"   تعداد دکمه‌ها: {len(buttons)}")
    for i, btn in enumerate(buttons):
        try:
            text = await btn.inner_text()
            print(f"   دکمه {i}: '{text}'")
        except:
            pass

    await context.close()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        await asyncio.gather(*[do_email(browser, e) for e in EMAILS])
        await browser.close()

asyncio.run(main())
