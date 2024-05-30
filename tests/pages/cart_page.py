from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_url = "https://www.amazon.de/-/en/cart?ref_=sw_gtc"

    def visit(self):
        self.page.goto(self.cart_url)

    def get_quantity(self):
        self.page.wait_for_selector("span[class='a-button a-button-dropdown quantity']")


    def update_quantity(self, new_quantity: str):
        self.page.click("span[class='a-button a-button-dropdown quantity']")
        self.page.click(f"li[aria-labelledby='quantity_{new_quantity}']")
        return new_quantity
    
    #comment3333
