import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.homepage import FergusonHomePage


"""	
Search for the Moen m6702bn from the search bar
@assert: That the product page we land on is what 
is expected by checking the product brand and product id
@difficulty Easy
"""


@pytest.mark.regressiontest
def test_search_product_lands_on_correct_product(browser):
    home_page = FergusonHomePage(browser)
    search_item = 'Moen m6702bn'
    expected_product_id = 'Part #M6702BN'
    expected_product_name = 'Moen'

    home_page.load_page()
    home_page.verify_title(home_page.PAGE_TITLE)
    home_page.search_item(search_item)
    home_page.verify_product_id(expected_product_id)
    home_page.verify_product_name(expected_product_name)
    home_page.verify_title(home_page.SEARCH_PAGE_TITLE)


"""
Go to the Bathroom Sinks category directly
(https://www.ferguson.com/category/bathroom-plumbing/bathroom-faucets/bathroom-sink-faucets/_/N-zbq4i3)
and add the second product on the search results (Category Drop) page to the cart.
@assert: the product that is added to the cart is what is expected
@difficulty Easy-Medium
"""


@pytest.mark.regressiontest
def test_add_product_to_cart_from_category_drop(browser):
    expected_product_name = 'Pfister Pfirst Series™ Single Handle Monoblock Bathroom Sink Faucet in Polished Chrome'

    home_page = FergusonHomePage(browser)
    home_page.navigate_to_the_page(home_page.BATHROOM_SINKS_URL)
    browser.find_element(By.XPATH, "//p[@data-placement='2']").click()
    home_page.click_add_to_cart_modal_button()
    home_page.verify_success_message_added_to_cart_displayed()
    home_page.verify_shopping_cart_amount("1")
    home_page.click_cart_icon()
    home_page.verify_expected_product_name(expected_product_name)

"""
Add two different finishes of a product (such as Moen m6702bn) to cart,
change the quantity of each finish on the cart page
@assert that the product and cart total update as expected when 
the quantity is changed
@difficulty Medium-Hard
"""

@pytest.mark.regressiontest
def test_add_multiple_cart_items_and_change_quantity(browser):
    home_page = FergusonHomePage(browser)
    search_item = 'Moen m6702bn'
    expected_product_id = 'Part #M6702BN'
    expected_product_name = 'Moen'

    home_page.load_page()
    home_page.verify_title(home_page.PAGE_TITLE)
    home_page.search_item(search_item)
    home_page.verify_product_id(expected_product_id)
    home_page.verify_product_name(expected_product_name)
    home_page.verify_title(home_page.SEARCH_PAGE_TITLE)
    home_page.click_add_cart_button()
    home_page.verify_shopping_cart_amount("1")
    home_page.click_chrome_finish()
    home_page.click_add_cart_button()
    home_page.verify_shopping_cart_amount("2")

