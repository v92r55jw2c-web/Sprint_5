from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    BUTTON_PERSONAL_ACCOUNT,
    BUTTON_LOGIN,
    BUTTON_ORDER,
    BUTTON_PROFILE_ON_PERSONAL_ACCOUNT,
    BUTTON_LOG_OUT
)

def test_log_out_from_personal_account(authorized_driver):
    driver = authorized_driver

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))

    driver.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_PROFILE_ON_PERSONAL_ACCOUNT))

    driver.find_element(*BUTTON_LOG_OUT).click()

    button_login = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_LOGIN))

    assert button_login.is_displayed()