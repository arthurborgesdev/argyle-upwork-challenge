from dotenv import dotenv_values

login_credentials = dotenv_values(".env")

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

PORTAL_LINK = login_credentials["PORTAL_LINK"]
USERNAME = login_credentials["USERNAME"]
PASSWORD = login_credentials["PASSWORD"]
SECRET = login_credentials["SECRET"]

def username_login(page):
    page.goto(PORTAL_LINK)
    page.fill('#login_username', USERNAME)
    page.click('#login_password_continue')

def password_login(page):
    page.fill('#login_password', PASSWORD)
    page.click('#login_control_continue')

def secret_login(page):
    page.fill('#login_answer', SECRET)
    page.click('#login_control_continue')

def scan_main_page(page):
    # interact to trigger auto-wait
    page.click("text=My Profile")
    current_page = page.content()
    print(get_visibility(current_page))
    
def get_visibility(current_page):
    main_portal = BeautifulSoup(current_page, 'html.parser') 
    visibility_div = main_portal.find_all("div", class_="fe-ui-profile-visibility-directive")
    for _vis in visibility_div:
        visibility_text = _vis.find(class_="ng-binding").string
    
    return visibility_text
   
def view_profile(page):
    page.click("text=View Profile")
    page.pause()
    current_page = page.content()


with sync_playwright() as p:
    # head with delay, so we don't need to solve reCaptcha
    browser = p.chromium.launch(headless=True, slow_mo=100)
    # Change this user_agent parameter based on your machine/envinroment
    context = browser.new_context(
        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    )
    page = context.new_page()

    username_login(page)
    password_login(page)
    # Add a verification to secret login here before
    # secret_login(page)
    scan_main_page(page)
    # view_profile(page)
    
    browser.close()


