# Сюда будем писать фикстуры
import pytest
from browser import *

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


@pytest.fixture
def standard_user():
    user = User('standard_user','secret_sauce')
    yield user


@pytest.fixture
def locked_out_user():
    user = User('locked_out_user','secret_sauce')
    yield user

@pytest.fixture
def problem_user():
    user = User('problem_user','secret_sauce')
    yield user

@pytest.fixture
def performance_glitch_user():
    user = User('performance_glitch_user','secret_sauce')
    yield user
@pytest.fixture
def error_user():
    user = User('error_user','secret_sauce')
    yield user

@pytest.fixture
def visual_user():
    user = User('visual_user','secret_sauce')
    yield user
@pytest.fixture
def browser():
    driver = Browser()
    driver.get_url()
    yield driver
    driver.close_browser()