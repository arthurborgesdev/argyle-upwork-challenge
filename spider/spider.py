from dotenv import dotenv_values

import cookies

login_credentials = dotenv_values(".env")

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

PORTAL_LINK = login_credentials["PORTAL_LINK"]
USERNAME = login_credentials["USERNAME"]
PASSWORD = login_credentials["PASSWORD"]
SECRET = login_credentials["SECRET"]

def username_login(page):
    page.goto(PORTAL_LINK)
    # print(context.cookies())
    page.screenshot(path="upwork.png")
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
    browser = p.chromium.launch(headless=True, slow_mo=100)
    context = browser.new_context(
        storage_state="state.json", 
        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    )
    page = context.new_page()
    # page.goto("https://bot.incolumitas.com")
    # page.screenshot(path="incolumitas.png")
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
