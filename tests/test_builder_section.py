from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    SECTION_BUNS,
    SECTION_BUNS_ACTIVE,
    SECTION_SAUCES,
    BUTTON_ORDER,
    SECTION_SAUCES_ACTIVE,
    SECTION_FILLINGS_ACTIVE,
    SECTION_FILLINGS
)

class TestConstructor:

    def test_go_to_section_buns(self, authorized_driver):
        driver = authorized_driver

        section_buns_element = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(SECTION_BUNS))

        driver.find_element(*SECTION_SAUCES).click()

        section_buns_element.click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(SECTION_BUNS_ACTIVE))


    def test_go_to_section_sauces(self, authorized_driver):
        driver = authorized_driver
    
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))
    
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(SECTION_BUNS))
    
        driver.find_element(*SECTION_SAUCES).click()
    
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(SECTION_SAUCES_ACTIVE))
    

    def test_go_to_section_fillings(self, authorized_driver):
        driver = authorized_driver
    
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))
    
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(SECTION_BUNS))
    
        driver.find_element(*SECTION_FILLINGS).click()
    
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(SECTION_FILLINGS_ACTIVE))