import pytest
import allure
from page.basket_page import BasketPage

@allure.feature("Проверка работы промокода")
@allure.story("Проверка, что цена после применения промокода уменьшается")
def test_check_promocode(page):
    basket_page = BasketPage(page)

    with allure.step("Открыть страницу и добавить товар в корзину"):
        basket_page.open()
        basket_page.add_first_item_to_cart()

    with allure.step("Получить цену до применения промокода"):
        price_before = basket_page.get_price_before()

    with allure.step("Применить промокод"):
        basket_page.click_have_promocode()
        basket_page.enter_promocode("genotek5")

    with allure.step("Получить цену после применения промокода"):
        price_after = basket_page.get_price_after()

    with allure.step("Проверка, что цена уменьшилась"):
        assert price_after < price_before, (
            f"Цена после применения промокода должна быть меньше. "
            f"До: {price_before} ₽, После: {price_after} ₽"
        )