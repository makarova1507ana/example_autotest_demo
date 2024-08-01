# сюда будем писать тесты

from conftest import *
from pages.loginPage import LoginPage

'''
standard_user 
locked_out_user
problem_user
performance_glitch_user
error_user
visual_user
'''
@pytest.mark.parametrize('username, password, expected_result', [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('error_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('visual_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')])

def test_loginPage( username, password, expected_result, browser):

    login_page = LoginPage(browser.driver)
    login_page.login(username, password)

    assert browser.current_url() == expected_result