from locators import *

new_password = '123456'

def register(driver, new_email):
    driver.find_element(*ENTER_AND_REGISTRATION).click()
    driver.find_element(*NO_ACCOUNT).click()

    driver.find_element(*EMAIL).send_keys(new_email)
    driver.find_element(*PASSWORD).send_keys(new_password)
    driver.find_element(*REPEAT_PASSWORD).send_keys(new_password)

    driver.find_element(*CREATE_ACCOUNT).click()


def login(driver, new_email):
    driver.find_element(*ENTER_AND_REGISTRATION).click()
    driver.find_element(*EMAIL).send_keys(new_email)
    driver.find_element(*PASSWORD).send_keys(new_password)
    driver.find_element(*LOGIN_BUTTON).click()
