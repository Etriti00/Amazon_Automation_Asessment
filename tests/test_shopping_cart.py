import time
import pytest
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("features/shopping_cart.feature")

@pytest.fixture
def context():
    return {}

@given("I open the Amazon homepage")
def navigate_to_homepage(page):
    home_page = HomePage(page)
    home_page.visit()
    time.sleep(2)

@when(parsers.parse('I enter "{product_name}" in the search field'))
def search_product(page, product_name):
    home_page = HomePage(page)
    home_page.search_for_product(product_name)
    time.sleep(2)

@when("I select the first search result")
def select_first_result(page):
    search_results_page = SearchResultsPage(page)
    search_results_page.click_first_result()
    time.sleep(2)

@when("I add the product to the cart")
def add_to_cart(page):
    product_details_page = ProductDetailsPage(page)
    product_details_page.add_to_cart()
    time.sleep(2)

@when("I navigate to the cart")
def navigate_to_cart(page):
    cart_page = CartPage(page)
    cart_page.visit()
    time.sleep(2)

@when(parsers.parse('I update the quantity of the product to "{new_quantity}"'))
def update_cart_quantity(page, new_quantity, context):
    cart_page = CartPage(page)
    cart_page.update_quantity(new_quantity)
    context['new_quantity'] = new_quantity
    time.sleep(2)

@then(parsers.parse('the cart should reflect the updated quantity "{quantity}"'))
def verify_updated_quantity(page, quantity, context):
    cart_page = CartPage(page)
    actual_quantity = cart_page.get_quantity()  
    