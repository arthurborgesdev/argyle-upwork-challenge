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

with sync_playwright() as p:
    # head with delay, so we don't need to solve reCaptcha
    browser = p.chromium.launch(headless=False, slow_mo=100) 
    page = browser.new_page()
    
    username_login(page)
    password_login(page)
    secret_login(page)
    
    print(page.title())
    browser.close()

soup = BeautifulSoup("<h1>Hello World!</h1>", 'html.parser')

# print(soup.prettify())

print(soup.h1.string)
