import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    BUTTON_PERSONAL_ACCOUNT,
    EMAIL_LOG_IN,
    PASSWORD_LOG_IN,
    BUTTON_LOGIN,
    BUTTON_ORDER
)
from data import TEST_EMAIL, TEST_PASSWORD, BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def authorized_driver(driver):
    driver.get(BASE_URL)

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(BUTTON_PERSONAL_ACCOUNT)).click()

    driver.find_element(*EMAIL_LOG_IN).send_keys(TEST_EMAIL)
    driver.find_element(*PASSWORD_LOG_IN).send_keys(TEST_PASSWORD)

    driver.find_element(*BUTTON_LOGIN).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))

    return driver
