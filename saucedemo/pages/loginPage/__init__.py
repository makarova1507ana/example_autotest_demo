# сюда будем писать описание страницы в виде класса
from .locators import *
class LoginPage:
    def __init__(self, driver):
        '''
        Parameters
        ----------
        driver - драйвер

        Поля класса(свойства):
        self.username  - поле на странице username
        self.password  - поле на странице password
        self.btn_login  - кнопка login на странице

        '''
        self.username = driver.find_element(*locator_username)
        self.password = driver.find_element(*locator_password)
        self.btn_login = driver.find_element(*locator_btn_login)

    def login(self, username, password):
        # Авторизация
        self.username.send_keys('standard_user')
        self.password.send_keys('secret_sauce')
        self.btn_login.click()