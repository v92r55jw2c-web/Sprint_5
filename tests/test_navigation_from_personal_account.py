from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    BUTTON_PERSONAL_ACCOUNT,
    BUTTON_ORDER,
    BUTTON_PROFILE_ON_PERSONAL_ACCOUNT,
    BUTTON_STELLAR_BURGERS,
    BUTTON_BUILDER
)


class TestNavigatoinPersonalAccount:

    def test_go_to_section_builder_on_StellarBurgers(self, authorized_driver):
        driver = authorized_driver

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))

        driver.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_PROFILE_ON_PERSONAL_ACCOUNT))

        driver.find_element(*BUTTON_STELLAR_BURGERS).click()

        button_order = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))

        assert button_order.is_displayed()



    def test_go_to_section_builder_on_buttonBuilder(self, authorized_driver):
        driver = authorized_driver

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))

        driver.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_PROFILE_ON_PERSONAL_ACCOUNT))

        driver.find_element(*BUTTON_BUILDER).click()

        button_order = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))

        assert button_order.is_displayed()

