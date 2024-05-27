class ProductDetailsPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button = "#add-to-cart-button"

    def add_to_cart(self):
        self.page.click(self.add_to_cart_button)