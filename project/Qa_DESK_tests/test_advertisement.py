from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from helper_func import *


def test_create_ad_unauthorized(driver):
    driver.find_element(*ADVERTISEMENT).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MESSAGE))

    assert driver.find_element(*MESSAGE).text == 'Чтобы разместить объявление, авторизуйтесь'


def test_create_ad_authorized(driver, new_email):
    register(driver, new_email)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(USER_NAME))

    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(ENTER_AND_REGISTRATION))

    login(driver, new_email)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(USER_NAME))

    driver.find_element(*ADVERTISEMENT).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(NAME_AD))

    driver.find_element(*NAME_AD).send_keys('Дом змей')
    driver.find_element(*CATEGORY_DROPDOWN).click()
    driver.find_element(*CATEGORY_AVTO).click()
    element = driver.find_element(*PUBLISH)
    driver.execute_script("arguments[0].scrollIntoView();", element)

    driver.find_element(*DESCRIPTION_AD).send_keys('Домик для змей')
    driver.find_element(*PRICE_AD).send_keys('5000')
    driver.find_element(*CITY_DROPDOWN).click()
    driver.find_element(*CITY_MSK).click()
    driver.find_element(*RADIO_NEW).click()

    driver.find_element(*PUBLISH).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(USER_AVATAR))

    driver.find_element(*USER_AVATAR).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(CREATE_AD))

    assert driver.find_element(*CREATE_AD).text == 'Дом змей'