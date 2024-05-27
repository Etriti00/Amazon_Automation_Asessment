class SearchResultsPage:
    def __init__(self, page):
        self.page = page
        self.first_result_selector = ".s-result-item .a-link-normal"

    def click_first_result(self):
        self.page.click(self.first_result_selector)
