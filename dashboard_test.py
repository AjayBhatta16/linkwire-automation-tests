import os
import uuid

from playwright.sync_api import Page, expect
from dotenv import load_dotenv

load_dotenv()

def before_each(page: Page):
    page.goto("https://app.linkwire.cc/login")

    page.get_by_test_id("username-input").fill(os.getenv("TEST_USERNAME"))
    page.get_by_test_id("password-input").fill(os.getenv("TEST_PASSWORD"))
    page.get_by_test_id("submit-button").click()

    page.wait_for_timeout(1000)

    expect(page).to_have_url("https://app.linkwire.cc/dashboard")

def test_create_link_succeeds(page: Page):
    before_each(page)

    initial_row_count = page.get_by_role("row").count()

    page.get_by_test_id("add-link-button").click()

    page.get_by_test_id("target-url-input").fill(os.getenv("TEST_TARGET_URL"))
    page.get_by_test_id("note-input").fill(str(uuid.uuid4()))
    page.get_by_test_id("submit-button").click()

    page.wait_for_timeout(1000)
    
    page.goto("https://app.linkwire.cc/dashboard")

    page.wait_for_timeout(1000)

    expect(page.get_by_role("row")).to_have_count(initial_row_count + 1)