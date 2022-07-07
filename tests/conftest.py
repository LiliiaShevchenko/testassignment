import allure
import pytest
import json
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


with open('./tests/configuration.json') as file:
    data = json.load(file)


@pytest.fixture()
def browser():
    if data['browser'] == 'chrome':
        if data['mode'] == 'headless':
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        else:
            browser = webdriver.Chrome(ChromeDriverManager().install())
    elif data['browser'] == "firefox":
        browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    # maximize browser window to full screen
    browser.maximize_window()
    yield browser
    # make a screenshot before closing the browser
    # allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    # when test is done, close ALL windows of the browser
    browser.quit()

