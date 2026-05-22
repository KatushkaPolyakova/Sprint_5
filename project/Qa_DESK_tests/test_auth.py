from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from helper_func import *


def test_registration(driver, new_email):
    register(driver, new_email)

    WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(user_name))

    assert driver.find_element(*user_name).is_displayed()
    assert driver.find_element(*user_avatar).is_displayed()


def test_registration_invalid_email(driver, new_email):
    driver.find_element(*enter_and_registration).click()
    driver.find_element(*no_account).click()

    driver.find_element(*email).send_keys(new_email[0:5])

    driver.find_element(*create_account).click()
    WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(email_error_text))

    assert driver.find_element(*email_error_text).text == "Ошибка"
    assert driver.find_element(*email_error).is_displayed()
    assert driver.find_element(*password_error).is_displayed()
    assert driver.find_element(*repeat_password_error).is_displayed()                                 


def test_registration_existing_user(driver, new_email):
    register(driver, new_email)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(user_name))

    driver.find_element(*logout_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(enter_and_registration))
    
    register(driver, new_email)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(email_error_text))

    assert driver.find_element(*email_error_text).text == "Ошибка"
    assert driver.find_element(*email_error).is_displayed()
    assert driver.find_element(*password_error).is_displayed()
    assert driver.find_element(*repeat_password_error).is_displayed()  

def test_login(driver, new_email):
    register(driver, new_email)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(user_name))

    driver.find_element(*logout_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(enter_and_registration))
    
    login(driver,new_email)

    WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(user_name))

    assert driver.find_element(*user_name).is_displayed()
    assert driver.find_element(*user_avatar).is_displayed()


def test_logout(driver, new_email):
    register(driver, new_email)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(user_name))

    driver.find_element(*logout_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(enter_and_registration))

    login(driver, new_email)

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(user_name))

    driver.find_element(*logout_button).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(enter_and_registration))

    assert driver.find_element(*enter_and_registration).is_displayed()

