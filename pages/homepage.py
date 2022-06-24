from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FergusonHomePage:

    def __init__(self, browser):
        self.browser = browser

    # URL and page title
    URL = 'https://www.ferguson.com/'
    BATHROOM_SINKS_URL = 'https://www.ferguson.com/category/bathroom-plumbing/bathroom-faucets/bathroom-sink-faucets/_/N-zbq4i3'
    PAGE_TITLE = 'Plumbing Supplies, HVAC Parts, Pipe, Valves & Fittings – Ferguson'
    SEARCH_PAGE_TITLE = 'Moen Genta™ Single Handle Centerset Bathroom Sink Faucet with Pop-Up Drain Assembly in Brushed Nickel - 6702BN - Ferguson'

    # Elements Locators
    SEARCH_FIELD = (By.NAME, "search")
    PRODUCT_NAME = (By.XPATH, "//h2[@itemprop='name']")
    PRODUCT_ID = (By.XPATH, "//span[@itemprop='productID']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".js-add-to-cart")
    ADD_TO_CART_MODAL_BUTTON = (By.XPATH,"//button[@data-form='addToCartModalForm']")
    SUCCESS_MESSAGE = (By.XPATH, "//span[contains(text(),'Added to your cart.')]")
    SHOPPING_CART_COUNT = (By.CLASS_NAME, "shoppingCartAmount")
    CART_ICON = (By.CLASS_NAME, "cart")
    SELECTED_PRODUCT_NAME = (By.CLASS_NAME, "product_name")
    CHROME_FINISH = (By.XPATH, "//img[@title='Chrome']")

    # Methods
    def load_page(self):
        self.browser.get(self.URL)
        WebDriverWait(self.browser, 10).until(
            lambda browser: browser.execute_script('return document.readyState') == 'complete')

    def verify_title(self, expected_title):
        assert expected_title in self.browser.title

    def search_item(self, item):
        search_input = self.browser.find_element(*self.SEARCH_FIELD)
        search_input.send_keys(item + Keys.RETURN)

    def verify_product_name(self, expected_product_name):
        product_name = WebDriverWait(self.browser, timeout=8).until(
            lambda d: d.find_element(*self.PRODUCT_NAME))
        assert product_name.text == expected_product_name

    def verify_product_id(self, product_id):
        el = WebDriverWait(self.browser, timeout=8).until(
            lambda d: d.find_element(*self.PRODUCT_ID))
        assert el.text == product_id

    def navigate_to_the_page(self, page_name):
        self.browser.get(page_name)
        WebDriverWait(self.browser, 10).until(
            lambda browser: browser.execute_script('return document.readyState') == 'complete')

    def find_item_and_click_by_number(self, number):
        pass

    def click_add_to_cart_modal_button(self):
        el = WebDriverWait(self.browser, timeout=8).until(
            lambda d: d.find_element(*self.ADD_TO_CART_MODAL_BUTTON))
        el.click()

    def verify_success_message_added_to_cart_displayed(self):
        success_message = self.browser.find_element(*self.SUCCESS_MESSAGE)
        assert success_message

    def verify_shopping_cart_amount(self, count):
        el = WebDriverWait(self.browser, timeout=8).until(
            lambda d: d.find_element(*self.SHOPPING_CART_COUNT))
        assert el.text == count

    def click_cart_icon(self):
        cart = WebDriverWait(self.browser, 8).until(
            EC.element_to_be_clickable((self.CART_ICON)))
        cart.click()

    def verify_expected_product_name(self, expected_product_name):
        product_name = WebDriverWait(self.browser, timeout=8).until(
            lambda d: d.find_element(*self.SELECTED_PRODUCT_NAME))
        assert product_name.text == expected_product_name

    def click_add_cart_button(self):
        add_to_cart_button = WebDriverWait(self.browser, timeout=15, poll_frequency=1).until(
            lambda d: d.find_element(*self.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()

    def click_chrome_finish(self):
        chrome_finish = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((self.CHROME_FINISH)))
        chrome_finish.click()