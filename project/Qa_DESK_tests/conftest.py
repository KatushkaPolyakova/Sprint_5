import pytest
import random
from selenium import webdriver
from locators import *


BASE_URL = 'https://qa-desk.education-services.ru/'


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()

@pytest.fixture
def new_email():
    return f'test{random.randint(1, 999999)}@mail.com'

