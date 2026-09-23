import asyncio
from playwright.async_api import async_playwright

async def test_site(browser, url, name):
    page = await browser.new_page()
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=15000)
        await asyncio.sleep(3)
        content = await page.content()
        print(f"[{name}] {url}")
        print(f"   طول محتوا: {len(content)}")
        print(f"   عنوان: {await page.title()}")
        
        # چاپ ۲۰۰ کاراکتر وسط صفحه
        print(f"   نمونه متن: {content[500:800]}")
        print()
    except Exception as e:
        print(f"[{name}] خطا: {e}")
    await page.close()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # تست چند سایت مختلف
        await test_site(browser, "https://example.com", "سایت ساده")
        await test_site(browser, "https://koalafaucet.com/doge", "koalafaucet")
        await test_site(browser, "https://httpbin.org/html", "httpbin")
        
        await browser.close()

asyncio.run(main())
