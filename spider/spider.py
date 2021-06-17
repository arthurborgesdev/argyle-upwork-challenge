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
              "Chrome/90.0.4430.93 Safari/537.36"
              )


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


class MainPage:

    def scan_main_page(self, page):
        # interact to trigger auto-wait
        page.click("text=My Profile")
        current_page = page.content()
        main_portal = BeautifulSoup(current_page, 'html.parser')
        print(self.get_visibility(main_portal))
        print(self.get_hours(main_portal))
        print(self.get_progress(main_portal))

    def get_visibility(self, soup, visibility_text="No visibility scanned"):
        visibility_div = soup.find_all("div",
                                              class_="fe-ui-profile-visibility"
                                              )
        for _vis in visibility_div:
            visibility_text = _vis.find(class_="ng-binding").string
        return visibility_text

    def get_hours(self, soup, hours_text="No hours scanned"):
        hours_div = soup.select("div.fe-ui-availability.ng-scope")
        for _hours in hours_div:
            hours_text = _hours.find(class_="ng-binding").string
        return hours_text

    def get_progress(self, soup, progress_text="No progress scanned"):
        progress_div = soup.find_all(class_="progress-bar")
        for _progress in progress_div:
            progress_text = _progress.find(class_="ng-binding").string
        return progress_text


class ProfilePage:

    def view_profile(self, page):
        page.click("text=View Profile")
        current_page = page.content()
        print(self.get_name(current_page))

    def get_name(current_page, name_text="No name scanned"):
        main_portal = BeautifulSoup(current_page, 'html.parser')
        name_div = main_portal.find_all(class_="progress-bar")
        for _name in name_div:
            name_text = _name.find(class_="ng-binding").string
        return name_text


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

    main = MainPage()
    main.scan_main_page(page)
    # profile = ProfilePage()
    # profile.view_profile(page)

    browser.close()
