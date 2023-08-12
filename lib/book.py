#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count

    def get_count(self):
        return self._page_count

    def set_count(self, page):
        if page == int:
            self._page = page
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    page_count = property(get_count, set_count,)
    
        