import os

from playwright.sync_api import Page, expect
from dotenv import load_dotenv

load_dotenv()

def test_redirect_succeeds(page: Page):
    page.goto(os.getenv("TEST_REDIRECT_URL"))

    page.wait_for_timeout(1000)

    expect(page).to_have_url(os.getenv("TEST_TARGET_URL"))