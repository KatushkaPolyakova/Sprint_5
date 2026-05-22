from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from helper_func import *


def test_create_ad_unauthorized(driver):
    driver.find_element(*advertisment).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(message))

    assert driver.find_element(*message).text == 'Чтобы разместить объявление, авторизуйтесь'


def test_create_ad_authorized(driver, new_email):
    register(driver, new_email)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(user_name))

    driver.find_element(*logout_button).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(enter_and_registration))

    login(driver, new_email)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(user_name))

    driver.find_element(*advertisment).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(name_ad))

    driver.find_element(*name_ad).send_keys('Дом змей')
    driver.find_element(*category_dropdown).click()
    driver.find_element(*category_avto).click()
    element = driver.find_element(*publish)
    driver.execute_script("arguments[0].scrollIntoView();", element)

    driver.find_element(*description_ad).send_keys('Домик для змей')
    driver.find_element(*price_av).send_keys('5000')
    driver.find_element(*city_dropdown).click()
    driver.find_element(*city_msk).click()
    driver.find_element(*radio_new).click()

    driver.find_element(*publish).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(user_avatar))

    driver.find_element(*user_avatar).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(created_ad))

    assert driver.find_element(*created_ad).text == 'Дом змей'