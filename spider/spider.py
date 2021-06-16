from dotenv import dotenv_values
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

login_credentials = dotenv_values(".env")

PORTAL_LINK = login_credentials["PORTAL_LINK"]
USERNAME = login_credentials["USERNAME"]
PASSWORD = login_credentials["PASSWORD"]
SECRET = login_credentials["SECRET"]
USER_AGENT = ("Mozilla/5.0 (X11; Linux x86_64)"
"AppleWebKit/537.36 (KHTML, like Gecko)"
"Chrome/90.0.4430.93 Safari/537.36")


class LoginHandling:

    def username_login(self, page):
        page.goto(PORTAL_LINK)
        page.fill('#login_username', USERNAME)
        page.click('#login_password_continue')

    def password_login(self, page):
        page.fill('#login_password', PASSWORD)
        page.click('#login_control_continue')

    def secret_login(self, page):
        page.fill('#login_answer', SECRET)
        page.click('#login_control_continue')


def scan_main_page(page):
    # interact to trigger auto-wait
    page.click("text=My Profile")
    current_page = page.content()
    print(get_visibility(current_page))
    print(get_hours(current_page))
    print(get_progress(current_page))


def get_visibility(current_page, visibility_text="No visibility scanned"):
    main_portal = BeautifulSoup(current_page, 'html.parser')
    visibility_div = main_portal.find_all("div",
                                          class_="fe-ui-profile-visibility"
                                          )
    for _vis in visibility_div:
        visibility_text = _vis.find(class_="ng-binding").string
    return visibility_text


def get_hours(current_page, hours_text="No hours scanned"):
    main_portal = BeautifulSoup(current_page, 'html.parser')
    hours_div = main_portal.select("div.fe-ui-availability.ng-scope")
    for _hours in hours_div:
        hours_text = _hours.find(class_="ng-binding").string
    return hours_text


def get_progress(current_page, progress_text="No progress scanned"):
    main_portal = BeautifulSoup(current_page, 'html.parser')
    progress_div = main_portal.find_all(class_="progress-bar")
    for _progress in progress_div:
        progress_text = _progress.find(class_="ng-binding").string
    return progress_text


def get_name(current_page, name_text="No name scanned"):
    main_portal = BeautifulSoup(current_page, 'html.parser')
    name_div = main_portal.find_all(class_="progress-bar")
    for _name in name_div:
        name_text = _name.find(class_="ng-binding").string
    return name_text


def view_profile(page):
    page.click("text=View Profile")
    current_page = page.content()
    print(get_name(current_page))


with sync_playwright() as p:
    # Apply slow_mo delay, so we don't need to solve reCaptcha
    browser = p.chromium.launch(headless=True, slow_mo=100)
    # Change this user_agent parameter based on your machine/envinroment
    context = browser.new_context(
        user_agent=USER_AGENT
    )
    page = context.new_page()
    login = LoginHandling()
    login.username_login(page)
    login.password_login(page)
    # Add a verification to secret login here before
    # secret_login(page)
    scan_main_page(page)
    # view_profile(page)

    browser.close()
