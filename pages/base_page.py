from playwright.sync_api import Page, Locator

class BasePage:
    MENU_WITH_LOWER_RESOLUTION = "Otwórz menu główne"
    DEVICES_LABEL = "Urządzenia"
    WITH_SUBSCRIPTION_LABEL = "Z abonamentem"
    SMARTPHONE_LABEL = "Smartfony"

    def __init__(self, page: Page):
        self.page = page
        self.page.add_locator_handler(self.page.get_by_role("button", name="Agree and close: Agree to our"), BasePage.handler, times=1)

    @staticmethod
    def handler(locator: Locator):
        locator.click()

    def click_menu_item(self, first_level: str, second_level: str, destination: str) -> None:
        nav = self.page.locator("#main-menu")
        main_menu_button = nav.get_by_role("button").filter(has_text=BasePage.MENU_WITH_LOWER_RESOLUTION)
        if main_menu_button.is_visible():
            main_menu_button.click()
            nav.get_by_role("button", name=first_level).click()
            nav.get_by_role("button", name=second_level).click()
            nav.get_by_role("link", name=destination, exact=True).click()
        else:
            nav.get_by_role("button", name=first_level).hover()
            second_locator = nav.locator(f'a:below(:text-is("{second_level}"))').filter(has_text=destination).first
            second_locator.click()

    def goto_smartphones_with_subscription(self) -> None:
        self.click_menu_item(BasePage.DEVICES_LABEL, BasePage.WITH_SUBSCRIPTION_LABEL, BasePage.SMARTPHONE_LABEL)