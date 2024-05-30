class HomePage:
    def __init__(self, page):
        self.page = page
        self.home_url = "https://www.amazon.de/"
        self.search_input = "#twotabsearchtextbox"

    def visit(self):
        self.page.goto(self.home_url)

    def search_for_product(self, product_name):
        self.page.wait_for_selector(self.search_input, state="visible")
        self.page.fill(self.search_input, product_name)
        self.page.press(self.search_input, 'Enter')