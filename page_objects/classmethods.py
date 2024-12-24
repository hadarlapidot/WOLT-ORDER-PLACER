from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random
import string


class ClassMethods:
    def __init__(self, driver: WebDriver):
        self._driver = driver

        # Locators
        self.login_button_locator = (By.XPATH, "//div[@class='s1zplo8']/following::button[1]")

        