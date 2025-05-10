from playwright.sync_api import Page, expect
import re


class StartPage:
    def __init__(self, page):
        self.page = page
        self.timeout = 500

    def toggle_favorite(self, book):
        # self.get_button("catalog").click(timeout=self.timeout)
        self.page.get_by_test_id('star-' + book).click(timeout=self.timeout)

    def add_book(self, author, book):
        self.get_button("add-book").click(timeout=self.timeout)

        self.page.get_by_test_id('add-input-title').fill(book)
        self.page.get_by_test_id('add-input-author').fill(author)

        expect(self.get_button('add-submit')).to_be_enabled()
        self.get_button('add-submit').click(timeout=self.timeout)

        self.page.get_by_test_id('catalog').click(timeout=self.timeout)

        expect(self.page.get_by_text(book)).to_be_visible()

    def get_book(self, book):
        # button = self.get_button('catalog')
        # if button.is_enabled():
        #     button.click(timeout=self.timeout)
        return self.page.get_by_text(book)

    def get_button(self, button, section=False):
        if section:
            self.page.get_by_test_id(section).click(timeout=self.timeout)
        return self.page.get_by_test_id(button)

def toggle_favorite(page, book):
    page.get_by_test_id('star-' + book).click(timeout=500)

