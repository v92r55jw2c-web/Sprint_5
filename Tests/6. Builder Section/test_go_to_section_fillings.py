from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    BUTTON_ORDER,
    SECTION_BUNS,
    SECTION_FILLINGS,
    SECTION_FILLINGS_ACTIVE
)

def test_go_to_section_fillings(authorized_driver):
    driver = authorized_driver

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(SECTION_BUNS))

    driver.find_element(*SECTION_FILLINGS).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(SECTION_FILLINGS_ACTIVE))


