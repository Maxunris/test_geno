import allure
from playwright.sync_api import Page

class BasketPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открыть страницу корзины")
    def open(self):
        self.page.goto("https://basket.genotek.ru/", wait_until="domcontentloaded")

    @allure.step("Добавить первый товар в корзину")
    def add_first_item_to_cart(self):
        self.page.get_by_role("link", name="Добавить в корзину").first.click()
        self.page.wait_for_timeout(3000)

    @allure.step("Получить цену до применения промокода")
    def get_price_before(self) -> float:
        price_text = self.page.locator("//div[2]/div/div[4]/span[2]/priceroller").text_content()
        price = self._clean_price(price_text)
        allure.attach(f"{price} ₽", name="Цена до применения промокода", attachment_type=allure.attachment_type.TEXT)
        return price

    @allure.step("Нажать 'У меня есть промокод'")
    def click_have_promocode(self):
        self.page.get_by_text("У меня есть промокод").click()

    @allure.step("Ввести промокод: {promocode}")
    def enter_promocode(self, promocode: str):
        self.page.get_by_placeholder("Введите промокод").click()
        self.page.get_by_placeholder("Введите промокод").fill(promocode)
        self.page.get_by_placeholder("Введите промокод").press("Enter")
        self.page.wait_for_timeout(3000)

    @allure.step("Получить цену после применения промокода")
    def get_price_after(self) -> float:
        price_text = self.page.locator("//div[2]/div/div[5]/span[2]/priceroller").text_content()
        price = self._clean_price(price_text)
        allure.attach(f"{price} ₽", name="Цена после применения промокода", attachment_type=allure.attachment_type.TEXT)
        return price

    def close(self):
        self.page.close()

    def _clean_price(self, price_text: str) -> float:
        clean_price = price_text.replace("₽", "").replace(" ", "").strip()
        return float(clean_price)