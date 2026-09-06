from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    BUTTON_PERSONAL_ACCOUNT,
    BUTTON_REGISTRATION_ON_PERSONAL_ACCOUNT,
    NAME,
    EMAIL,
    PASSWORD,
    BUTTON_REGISTRATION,
    BUTTON_LOGIN,
    PASSWORD_ERROR
)
from data import BASE_URL
from utils import generate_email, generate_password



class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(BASE_URL)
        
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(BUTTON_PERSONAL_ACCOUNT)).click()
        
        driver.find_element(*BUTTON_REGISTRATION_ON_PERSONAL_ACCOUNT).click()
        driver.find_element(*NAME).send_keys("Оля")
        
        email = generate_email()
        driver.find_element(*EMAIL).send_keys(email)

        password = generate_password()
        driver.find_element(*PASSWORD).send_keys(password)
        
        driver.find_element(*BUTTON_REGISTRATION).click()
        
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_LOGIN))
        
        assert driver.current_url.endswith("/login")


        
    def test_registration_with_incorrect_password(self, driver):
        driver.get(BASE_URL)
    
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(BUTTON_PERSONAL_ACCOUNT)).click()
    
        driver.find_element(*BUTTON_REGISTRATION_ON_PERSONAL_ACCOUNT).click()
        driver.find_element(*NAME).send_keys("Оля")
    
        email = generate_email()
        driver.find_element(*EMAIL).send_keys(email)
        
        password = "12345"
        driver.find_element(*PASSWORD).send_keys(password)
    
        driver.find_element(*BUTTON_REGISTRATION).click()
    
        password_error = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(PASSWORD_ERROR))
    
        assert password_error.text == "Некорректный пароль"