import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.timeout = 3
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser
