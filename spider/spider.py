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
    print(context.cookies())
    page.screenshot(path="screenshot.png")
    page.fill('#login_username', USERNAME)
    page.click('#login_password_continue')

def password_login(page):
    page.fill('#login_password', PASSWORD)
    page.click('#login_control_continue')

def secret_login(page):
    page.fill('#login_answer', SECRET)
    page.click('#login_control_continue')

def view_profile(page):
    page.click("text=View Profile")
    page.pause()
    current_page = browser.page_source
    my_profile = BeautifulSoup(page, 'html.parser') 
    print(my_profile.h1.string)

with sync_playwright() as p:
    # head with delay, so we don't need to solve reCaptcha
    browser = p.chromium.launch()
    context = browser.new_context()
    context.add_cookies([
        {
            'name': 'visitor_signup_gql_token',
            'value': 'oauth2v2_7a89c810d2e1ab969420a3d6b212e39d',
            'domain': '.upwork.com',
            'path': '/',
            'expires': -1,
            'httpOnly': False,
            'secure': True,
            'sameSite': 'None',
        }
    ])

    page = context.new_page()
    
    username_login(page)
    #password_login(page)
    # Add a verification to secret login here before
    # secret_login(page)
    #view_profile(page)
    
    #print(page.title())
    browser.close()

soup = BeautifulSoup("<h1>Hello World!</h1>", 'html.parser')

# print(soup.prettify())

print(soup.h1.string)
