from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    BUTTON_PERSONAL_ACCOUNT,
    BUTTON_ORDER,
    BUTTON_PROFILE_ON_PERSONAL_ACCOUNT
)

def test_go_to_personal_account(authorized_driver):
    driver = authorized_driver

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))

    driver.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    button_profile_account = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_PROFILE_ON_PERSONAL_ACCOUNT))

    assert button_profile_account.is_displayed()