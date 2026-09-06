from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
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

class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(BUTTON_PERSONAL_ACCOUNT)).click()
        
        driver.find_element(*BUTTON_REGISTRATION_ON_PERSONAL_ACCOUNT).click()
        driver.find_element(*NAME).send_keys("Оля")
        
        email = f"{random.randint(100000, 999999)}@yandex.ru"
        driver.find_element(*EMAIL).send_keys(email)
        
        password = f"{random.randint(100000, 999999)}"
        driver.find_element(*PASSWORD).send_keys(password)
        
        driver.find_element(*BUTTON_REGISTRATION).click()
        
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON_LOGIN))
        
        assert driver.current_url.endswith("/login")


        
    def test_registration_with_incorrect_password(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
    
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(BUTTON_PERSONAL_ACCOUNT)).click()
    
        driver.find_element(*BUTTON_REGISTRATION_ON_PERSONAL_ACCOUNT).click()
        driver.find_element(*NAME).send_keys("Оля")
    
        email = f"{random.randint(100000, 999999)}@yandex.ru"
        driver.find_element(*EMAIL).send_keys(email)
    
        password = f"{random.randint(10000, 99999)}"
        driver.find_element(*PASSWORD).send_keys(password)
    
        driver.find_element(*BUTTON_REGISTRATION).click()
    
        password_error = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(PASSWORD_ERROR))
    
        assert password_error.text == "Некорректный пароль"