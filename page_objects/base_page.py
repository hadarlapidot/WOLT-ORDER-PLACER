from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.classmethods import ClassMethods


class BasePage(ClassMethods):
    def __init__(self, driver):
        super().__init__(driver)

    
    # assumes in home page: returns true if the log in button is visible
    def is_logged_in(self):
        return ec.presence_of_element_located(self.login_button_locator)
    
    def log_in(self):
        self._driver.find_element(self.login_button_locator).click()