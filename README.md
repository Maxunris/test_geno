Для установки вводить:
pip install pytest pytest-playwright allure-pytest
playwright install


Для запуска тестов:
pytest --alluredir=allure-results


Для создания отчета:
allure serve allure-results


Если нужно видеть как идут тесты, в файле conftest  в стоке browser = p.chromium.launch(headless=True) поменять True на False


![Отчетность.png](%D0%9E%D1%82%D1%87%D0%B5%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C.png)

