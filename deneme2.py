import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

PROFILE_DIR = Path.home() / "selenium_chrome_profile"

async def open_whatsapp():
    print("[1] Playwright başlatılıyor")

    async with async_playwright() as p:
        print("[2] Persistent context açılıyor")
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = context.pages[0] if context.pages else await context.new_page()

        print("[3] WhatsApp Web açılıyor")
        await page.goto("https://web.whatsapp.com")

        print("[✓] Eğer login cookie geçerliyse QR sormadan açılacak")
        await page.wait_for_timeout(10000)

        print("[✓] Test tamam")
        # context.close()  # kapatma, session kalsın

asyncio.run(open_whatsapp())
