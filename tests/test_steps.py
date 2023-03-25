import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "nasedkinds")
@allure.feature("поиск Issue")
@allure.story("оформление теста allure.step")
@allure.link("https://github.com", name="Testing")
def test_github():
    with allure.step('Перейти на сайт'):
        browser.open('https://github.com')
    with allure.step('Открыть браузер на максимальный размер'):
        browser.driver.maximize_window()

    with allure.step('поиск репозитория'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()

    with allure.step('переход на репозиторий'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('переход на закладку Issues'):
        s('#issues-tab').click()

    with allure.step('проверка Issue 81'):
        s(by.partial_text('#81')).should(be.visible)