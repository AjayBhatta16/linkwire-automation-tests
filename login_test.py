import os
import uuid

from playwright.sync_api import Page, expect

def test_login_succeeds_with_username(page: Page):
    page.goto("https://app.linkwire.cc")

    page.get_by_test_id("login-button").click()

    expect(page).to_have_url("https://app.linkwire.cc/login")

    page.get_by_test_id("username-input").fill(os.getenv("TEST_USERNAME"))
    page.get_by_test_id("password-input").fill(os.getenv("TEST_PASSWORD"))
    page.get_by_test_id("submit-button").click()

    expect(page).to_have_url("https://app.linkwire.cc/dashboard")

def test_login_succeeds_with_email(page: Page):
    page.goto("https://app.linkwire.cc")

    page.get_by_test_id("login-button").click()

    expect(page).to_have_url("https://app.linkwire.cc/login")

    page.get_by_test_id("username-input").fill(os.getenv("TEST_EMAIL"))
    page.get_by_test_id("password-input").fill(os.getenv("TEST_PASSWORD"))
    page.get_by_test_id("submit-button").click()

    expect(page).to_have_url("https://app.linkwire.cc/dashboard")

def test_login_fails_invalid_username(page: Page):
    page.goto("https://app.linkwire.cc")

    page.get_by_test_id("login-button").click()

    expect(page).to_have_url("https://app.linkwire.cc/login")

    page.get_by_test_id("username-input").fill(str(uuid.uuid4()))
    page.get_by_test_id("password-input").fill(os.getenv("TEST_PASSWORD"))
    page.get_by_test_id("submit-button").click()

    expect(page).to_have_url("https://app.linkwire.cc/login")

def test_login_fails_invalid_password(page: Page):
    page.goto("https://app.linkwire.cc")

    page.get_by_test_id("login-button").click()

    expect(page).to_have_url("https://app.linkwire.cc/login")

    page.get_by_test_id("username-input").fill(os.getenv("TEST_USERNAME"))
    page.get_by_test_id("password-input").fill(str(uuid.uuid4()))
    page.get_by_test_id("submit-button").click()

    expect(page).to_have_url("https://app.linkwire.cc/login")