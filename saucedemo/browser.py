# Сюда будем писать все что связано с драйвером
from selenium import webdriver

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'https://www.saucedemo.com/'

    def get_url(self, url=''):
        if url == '':
            url = self.base_url
        self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

    def close_browser(self):
        self.driver.close()