from playwright.sync_api import sync_playwright
import playwright
import json

# other support files
from scanner.login import LoginHandling
from scanner.targets import User, MainPage, ProfilePage

# For type annotations
from playwright.sync_api import Page

user_agent = ("Mozilla/5.0 (X11; Linux x86_64)"
              "AppleWebKit/537.36 (KHTML, like Gecko)"
              "Chrome/90.0.4430.93 Safari/537.36"
              )


def login_handle(page: Page) -> None:
    login = LoginHandling()
    login.username(page)
    login.password(page)
    login.secret(page)


def scan_page(user: User, page: Page) -> None:
    main = MainPage(user)
    main.scan(page)
    profile = ProfilePage(user)
    profile.scan(page)


def initiate_scan() -> None:
    with sync_playwright() as p:
        # Apply slow_mo delay, so we don't need to solve reCaptcha
        browser = p.chromium.launch(headless=True, slow_mo=100)
        # Change this user_agent parameter based on your machine/envinroment
        context = browser.new_context(
            user_agent=user_agent
        )
        page = context.new_page()

        login_handle(page)

        user = User()
        scan_page(user, page)

        with open('scan_data.json', 'w') as outfile:
            json.dump(user.dict(), outfile)

        browser.close()


if __name__ == "__main__":
    while True:
        try:
            initiate_scan()
            break
        except (playwright._impl._api_types.TimeoutError, AttributeError,
                UnboundLocalError) as e:
            print(e)
            print("An error occurred... restarting.")
