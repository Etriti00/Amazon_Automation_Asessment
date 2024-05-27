from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self):
        self.page.goto("https://www.amazon.com")

    def search_for_product(self, product_name):
        self.page.fill('input[name="field-keywords"]', product_name)
        self.page.press('input[name="field-keywords"]', 'Enter')

class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page

    def click_first_result(self):
        self.page.click('.s-result-item .a-link-normal')

class ProductDetailsPage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_cart(self):
        self.page.click('#add-to-cart-button')

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self):
        self.page.goto("https://www.amazon.com/gp/cart/view.html")

    def update_quantity(self, new_quantity):
        self.page.select_option('#dropdown1', new_quantity)

    def get_quantity(self):
        return self.page.inner_text('#dropdown1')