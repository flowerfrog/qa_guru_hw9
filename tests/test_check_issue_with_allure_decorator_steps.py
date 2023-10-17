import time

import allure
from allure_commons.types import Severity, AttachmentType
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "flowerfrog")
@allure.feature("Задачи в репозитории")
@allure.story("Поиск Issue")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository("flowerfrog/stepik_auto_tests_course")
    go_to_repository("flowerfrog/stepik_auto_tests_course")
    open_issue_tab()
    should_see_issue_with_name("test_issue")


@allure.step("Открываем браузер")
def open_main_page():
    browser.open('https://github.com/')


@allure.step("Ищем репозиторий")
def search_for_repository(repo):
    s(".search-input").click()
    s("#query-builder-test").send_keys(repo).press_enter()


@allure.step("Переходим по ссылке в репозиторий")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Переходим в таб Issue")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issuе с названием test_issue")
def should_see_issue_with_name(name):
    s(by.partial_text(name)).should(be.visible)


browser.quit()
