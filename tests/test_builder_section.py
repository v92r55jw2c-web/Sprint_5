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

        section_buns_active = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(SECTION_BUNS_ACTIVE))

        assert section_buns_active.is_displayed()



    def test_go_to_section_sauces(self, authorized_driver):
        driver = authorized_driver
    
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))
    
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(SECTION_BUNS))
    
        driver.find_element(*SECTION_SAUCES).click()
    
        section_sauces_active = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(SECTION_SAUCES_ACTIVE))

        assert section_sauces_active.is_displayed()
    

    def test_go_to_section_fillings(self, authorized_driver):
        driver = authorized_driver
    
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_ORDER))
    
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(SECTION_BUNS))
    
        driver.find_element(*SECTION_FILLINGS).click()
    
        section_fillings_active = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(SECTION_FILLINGS_ACTIVE))

        assert section_fillings_active.is_displayed()