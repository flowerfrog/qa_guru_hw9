import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открываем браузер"):
        browser.open('https://github.com/')
    with allure.step("Ищем репозиторий"):
        s(".search-input").click()
        s("#query-builder-test").send_keys("flowerfrog/stepik_auto_tests_course").press_enter()
    with allure.step("Переходим по ссылке в репозиторий"):
        s(by.link_text("flowerfrog/stepik_auto_tests_course")).click()
    with allure.step("Переходим в таб Issue"):
        s("#issues-tab").click()
    with allure.step("Проверяем наличие Issuе с названием test_issue"):
        s(by.partial_text("test_issue")).should(be.visible)
    browser.quit()
