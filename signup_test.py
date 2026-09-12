import os
import uuid

from playwright.sync_api import Page, expect
from dotenv import load_dotenv

load_dotenv()

def test_signup_succeeds(page: Page):
    page.goto("https://app.linkwire.cc")

    page.get_by_test_id("signup-button").click()

    expect(page).to_have_url("https://app.linkwire.cc/signup")

    username = f"playwright_{uuid.uuid4()}"

    page.get_by_test_id("username-input").fill(username)
    page.get_by_test_id("email-input").fill(f"{username}@dne.dne")
    page.get_by_test_id("password-input").fill("linkwire")
    page.get_by_test_id("agreed-to-latest-terms-checkbox")\
        .locator('input[type="checkbox"]').click()
    page.get_by_test_id("submit-button").click()

    page.wait_for_timeout(1000)

    expect(page).to_have_url("https://app.linkwire.cc/dashboard")

def test_signup_fails_duplicate_username(page: Page):
    page.goto("https://app.linkwire.cc")

    page.get_by_test_id("signup-button").click()

    expect(page).to_have_url("https://app.linkwire.cc/signup")

    page.get_by_test_id("username-input").fill(os.getenv("TEST_USERNAME"))
    page.get_by_test_id("email-input").fill(f"{uuid.uuid4()}@dne.dne")
    page.get_by_test_id("password-input").fill("linkwire")
    page.get_by_test_id("agreed-to-latest-terms-checkbox")\
        .locator('input[type="checkbox"]').click()
    page.get_by_test_id("submit-button").click()

    page.wait_for_timeout(1000)

    expect(page).to_have_url("https://app.linkwire.cc/signup")

def test_signup_fails_duplicate_email(page: Page):
    page.goto("https://app.linkwire.cc")

    page.get_by_test_id("signup-button").click()

    expect(page).to_have_url("https://app.linkwire.cc/signup")

    page.get_by_test_id("username-input").fill(f"playwright_{uuid.uuid4()}")
    page.get_by_test_id("email-input").fill(os.getenv("TEST_EMAIL"))
    page.get_by_test_id("password-input").fill("linkwire")
    page.get_by_test_id("agreed-to-latest-terms-checkbox")\
        .locator('input[type="checkbox"]').click()
    page.get_by_test_id("submit-button").click()

    page.wait_for_timeout(1000)

    expect(page).to_have_url("https://app.linkwire.cc/signup")