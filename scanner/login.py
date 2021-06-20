from dotenv import dotenv_values
from playwright.sync_api import Page
import playwright

login_credentials = dotenv_values(".env")

portal_link = login_credentials["PORTAL_LINK"]
username = login_credentials["USERNAME"]
password = login_credentials["PASSWORD"]
secret = login_credentials["SECRET"]


class LoginHandling:

    def username_login(self, page: Page) -> None:
        page.goto(portal_link)
        page.fill('#login_username', username)
        page.click('#login_password_continue')

    def password_login(self, page: Page) -> None:
        page.fill('#login_password', password)
        page.click('#login_control_continue')

    def secret_login(self, page: Page) -> None:
        try:
            page.wait_for_selector("text=Let's make sure it's you", timeout=5)
            page.fill('#login_answer', secret)
            page.click('#login_control_continue')
        except playwright._impl._api_types.TimeoutError:
            pass
