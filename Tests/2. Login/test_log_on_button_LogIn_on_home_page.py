
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    BUTTON_LOGIN_HOME_PAGE,
    BUTTON_PERSONAL_ACCOUNT,
    EMAIL_LOG_IN,
    PASSWORD_LOG_IN,
    BUTTON_LOGIN,
    BUTTON_ORDER
)

def test_log_on_button_LogIn_on_home_page(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*BUTTON_LOGIN_HOME_PAGE).click()

    driver.find_element(*EMAIL_LOG_IN).send_keys("olya_mikheeva_53_001@yandex.ru")
    driver.find_element(*PASSWORD_LOG_IN).send_keys("123456789")

    driver.find_element(*BUTTON_LOGIN).click()

    button_order = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))

    assert button_order.is_displayed()