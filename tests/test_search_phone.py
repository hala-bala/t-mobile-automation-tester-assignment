import pytest
from playwright.sync_api import Page

from pages.devices_page import DevicePage
from pages.home_page import HomePage
from pages.phone_page import PhonePage


@pytest.mark.only_browser("chromium")
@pytest.mark.parametrize("manufacturer,model,color", [("Apple", "iPhone 15", "Niebieski")])
def test_search_phone_available(page: Page, manufacturer: str, model: str, color:str):
    #given

    #when
    page.goto("https://www.t-mobile.pl/")
    home = HomePage(page)
    home.goto_smartphones_with_subscription()
    devices = DevicePage(page)
    devices.filter_devices_by_manufacturer(manufacturer)
    devices.find_model(model)
    phone = PhonePage(page)
    is_phone_visible = phone.is_available(color)

    #then
    assert is_phone_visible == True, f"Model {model} from {manufacturer} in color {color} is not available for devices with subscription"