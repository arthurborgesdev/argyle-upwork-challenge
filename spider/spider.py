from playwright.sync_api import sync_playwright
import json

# other support files
from login import LoginHandling
from targets import User, MainPage, ProfilePage

user_agent = ("Mozilla/5.0 (X11; Linux x86_64)"
              "AppleWebKit/537.36 (KHTML, like Gecko)"
              "Chrome/90.0.4430.93 Safari/537.36"
              )

def login_routine(page):
    login = LoginHandling()
    login.username_login(page)
    login.password_login(page)
    login.secret_login(page)

def scan_routine(user, page):
    main = MainPage(user)
    main.scan_main_page(page)
    profile = ProfilePage(user)
    profile.scan_profile_page(page)

with sync_playwright() as p:
    # Apply slow_mo delay, so we don't need to solve reCaptcha
    browser = p.chromium.launch(headless=True, slow_mo=100)
    # Change this user_agent parameter based on your machine/envinroment
    context = browser.new_context(
        user_agent=user_agent
    )
    page = context.new_page()

    login_routine(page)
    user = User()
    scan_routine(user, page)

    with open('scan_data.json', 'w') as outfile:
        json.dump(user.dict(), outfile)

    browser.close()
