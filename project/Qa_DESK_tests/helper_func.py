from locators import *

new_password = '123456'

def register(driver, new_email):
    driver.find_element(*enter_and_registration).click()
    driver.find_element(*no_account).click()

    driver.find_element(*email).send_keys(new_email)
    driver.find_element(*password).send_keys(new_password)
    driver.find_element(*repeat_password).send_keys(new_password)

    driver.find_element(*create_account).click()


def login(driver, new_email):
    driver.find_element(*enter_and_registration).click()
    driver.find_element(*email).send_keys(new_email)
    driver.find_element(*password).send_keys(new_password)
    driver.find_element(*login_button).click()
