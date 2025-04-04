from playwright.sync_api import Page

from pages.base_page import BasePage


class DevicePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def filter_devices_by_manufacturer(self, manufacturer: str):
        manufacturer_locator = self.page.get_by_label(manufacturer)
        manufacturer_locator.click()

    def find_model(self, model: str):
        model_div = self.page.locator(f'section').filter(has_text=model).locator("..")
        model_div.click()
        self.page.wait_for_selector(".rowWrapper")

