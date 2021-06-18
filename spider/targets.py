from bs4 import BeautifulSoup  # type: ignore
from pydantic import BaseModel
from typing import Any, Tuple, Dict

# For type annotations
from playwright.sync_api import Page

class Address(Dict[str, Any]):
    line1: str = ''
    line2: str = ''
    city: str = ''
    state: str = ''
    postal_code: str = ''
    country: str = ''


class User(BaseModel):
    visibility: str = ''
    work_hours: str = ''
    progress: str = ''
    first_name: str = ''
    last_name: str = ''
    full_name: str = ''
    picture_url: str = ''
    address: Address = {}


class MainPage:
    def __init__(self, user: User) -> None:
        self.user = user

    def scan_main_page(self, page: Page) -> None:
        # interact to trigger auto-wait
        page.click("text=My Profile")
        current_page = page.content()
        main_page = BeautifulSoup(current_page, 'lxml')
        self.user.visibility = self.get_visibility(main_page)
        self.user.work_hours = self.get_hours(main_page)
        self.user.progress = self.get_progress(main_page)

    def get_visibility(self, soup: BeautifulSoup) -> str:
        visibility_div = soup.find_all("div",
                                       class_="fe-ui-profile-visibility"
                                       )
        for _vis in visibility_div:
            visibility_text = "No visibility scanned"
            try:
                visibility_text = _vis.find(class_="ng-binding").string
            except AttributeError:
                continue
        return visibility_text

    def get_hours(self, soup: BeautifulSoup) -> str:
        hours_div = soup.select("div.fe-ui-availability.ng-scope")
        for _hours in hours_div:
            hours_text = "No work hours scanned"
            try:
                hours_text = _hours.find(class_="ng-binding").string
            except AttributeError:
                continue
        return hours_text

    def get_progress(self, soup: BeautifulSoup) -> str:
        progress_div = soup.find_all(class_="progress-bar")
        # print(progress_div) # Random bug of displaying
        # lots and lots of progress classes together
        for _progress in progress_div:
            progress_text = "No progress scanned"
            try:
                progress_text = _progress.find(class_="ng-binding").string
            except AttributeError:
                continue
        return progress_text


class ProfilePage:
    def __init__(self, user: User) -> None:
        self.user = user

    def scan_profile_page(self, page: Page) -> None:
        # First click to access the page
        page.click("text=View Profile")
        # Second click to trigger auto-wait until page finishes rendering
        page.click("text=View Profile")
        current_page = page.content()
        profile_page = BeautifulSoup(current_page, 'lxml')
        (self.user.first_name,
         self.user.last_name,
         self.user.full_name) = self.get_name(profile_page)
        self.user.picture_url = self.get_picture_url(profile_page)
        (self.user.address['line1'],
         self.user.address['line2'],
         self.user.address['city'],
         self.user.address['state'],
         self.user.address['postal_code'],
         self.user.address['country']) = self.get_address(profile_page)

    def get_name(self, soup: BeautifulSoup) -> Tuple[str, str, str]:
        name_text = ""
        try:
            name_text_find = soup.find_all(class_="identity-content")
            name_text = name_text_find[0].h1.string.strip()
        except AttributeError:
            first_name = "No first name scanned"
            last_name = "No last name scanned"
            full_name = "No full name scanned"
            return first_name, last_name, full_name
        first_name = name_text.split()[0]
        last_name = name_text.split()[1]
        full_name = name_text
        return first_name, last_name, full_name

    def get_picture_url(self, soup: BeautifulSoup) -> str:
        picture_div = soup.find_all(class_="cfe-ui-profile-identity")[0]
        picture_url = "No picture scanned"
        try:
            picture_url = picture_div.find(class_="up-avatar")['src']
        except AttributeError:
            pass
        return picture_url

    def get_address(self, soup: BeautifulSoup) \
            -> Tuple[str, str, str, str, str, str]:
        address_div = soup.find_all(class_="identity-content")[0]
        line1 = "No address line1 scanned"
        line2 = "No address line2 scanned"
        address_city = "No address scanned"
        state = "No state scanned"
        postal_code = "No postal code scanned"
        address_country = "No country scanned"
        try:
            address_city_select = address_div.\
                select('span[itemprop="locality"]')
            address_city = address_city_select[0].string.title()
            address_country_select = address_div.\
                select('span[itemprop="country-name"]')
            address_country = address_country_select[0].string.title()
        except AttributeError:
            pass
        return line1, line2, address_city, state, postal_code, address_country