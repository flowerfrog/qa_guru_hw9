from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_selene():
    browser.open('https://github.com/')
    s(".search-input").click()
    s("#query-builder-test").send_keys("flowerfrog/stepik_auto_tests_course").press_enter()
    s(by.link_text("flowerfrog/stepik_auto_tests_course")).click()
    s("#issues-tab").click()
    s(by.partial_text("test_issue")).should(be.visible)
    browser.quit()


