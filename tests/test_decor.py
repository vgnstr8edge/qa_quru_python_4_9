import allure
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "nasedkinds")
@allure.feature("поиск Issue")
@allure.story("оформление теста декораторами")
@allure.link("https://github.com", name="Testing")
def test_decor():
    open_website()
    search_of_repo('eroshenkoam/allure-example')
    go_to_repo('eroshenkoam/allure-example')
    open_issue()
    should_see_ish_and_num('#81')


@allure.step('Перейти на сайт')
def open_website():
    browser.open('https://github.com')
    browser.driver.maximize_window()


@allure.step('поиск репозитория {repo}')
def search_of_repo(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()


@allure.step('переход на репозиторий {repo}')
def go_to_repo(repo):
    s(by.link_text(repo)).click()


@allure.step('переход на закладку Issues')
def open_issue():
    s('#issues-tab').click()


@allure.step('проверка Issue {number}')
def should_see_ish_and_num(number):
    s(by.partial_text(number)).click()