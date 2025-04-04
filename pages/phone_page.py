from playwright.sync_api import Page, Error, Locator

from pages.base_page import BasePage


class PhonePage(BasePage):
    AVAILABLE_LABEL = "Dostępny"

    def __init__(self, page: Page):
        super().__init__(page)

    def is_available(self, color: str) -> bool:
        try:
            color_divs = self.page.locator(".dt_variant")
            color_div = PhonePage.__found_color(color_divs, color)
            if color_div:
                color_div.click()
                self.page.wait_for_selector(f'.selectedColor:has-text("{color}")')
            else:
                return False
            return self.page.locator(".rowWrapper").locator("..").get_by_text(PhonePage.AVAILABLE_LABEL, exact=True).is_visible()
        except Error:
            return False

    @staticmethod
    def __found_color(color_divs: Locator, color: str) -> Locator | None:
        for color_div in color_divs.all():
            color_div.hover()
            if color_div.get_by_text(color).is_visible():
                return color_div
        return None
