from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from helper_func import *


def test_registration(driver, new_email):
    register(driver, new_email)

    WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(USER_NAME))

    assert driver.find_element(*USER_NAME).is_displayed()
    assert driver.find_element(*USER_AVATAR).is_displayed()


def test_registration_invalid_email(driver, new_email):
    driver.find_element(*ENTER_AND_REGISTRATION).click()
    driver.find_element(*NO_ACCOUNT).click()

    driver.find_element(*EMAIL).send_keys(new_email[0:5])

    driver.find_element(*CREATE_ACCOUNT).click()
    WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(EMAIL_ERROR_TEXT))

    assert driver.find_element(*EMAIL_ERROR_TEXT).text == "Ошибка"
    assert driver.find_element(*EMAIL_ERROR).is_displayed()
    assert driver.find_element(*PASSWORD_ERROR).is_displayed()
    assert driver.find_element(*REPEAT_PASSWORD_ERROR).is_displayed()                                 


def test_registration_existing_user(driver, new_email):
    register(driver, new_email)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(USER_NAME))

    driver.find_element(*LOGOUT_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(ENTER_AND_REGISTRATION))
    
    register(driver, new_email)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(EMAIL_ERROR_TEXT))

    assert driver.find_element(*EMAIL_ERROR_TEXT).text == "Ошибка"
    assert driver.find_element(*EMAIL_ERROR).is_displayed()
    assert driver.find_element(*PASSWORD_ERROR).is_displayed()
    assert driver.find_element(*REPEAT_PASSWORD_ERROR).is_displayed()  

def test_login(driver, new_email):
    register(driver, new_email)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(USER_NAME))

    driver.find_element(*LOGOUT_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(ENTER_AND_REGISTRATION))
    
    login(driver,new_email)

    WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(USER_NAME))

    assert driver.find_element(*USER_NAME).is_displayed()
    assert driver.find_element(*USER_AVATAR).is_displayed()


def test_logout(driver, new_email):
    register(driver, new_email)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(USER_NAME))

    driver.find_element(*LOGOUT_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(ENTER_AND_REGISTRATION))

    login(driver, new_email)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(USER_NAME))

    driver.find_element(*LOGOUT_BUTTON).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(ENTER_AND_REGISTRATION))

    assert driver.find_element(*ENTER_AND_REGISTRATION).is_displayed()

