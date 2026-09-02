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

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def authorized_driver(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(BUTTON_PERSONAL_ACCOUNT)).click()

    driver.find_element(*EMAIL_LOG_IN).send_keys("olya_mikheeva_53_001@yandex.ru")
    driver.find_element(*PASSWORD_LOG_IN).send_keys("123456789")

    driver.find_element(*BUTTON_LOGIN).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))

    return driver
