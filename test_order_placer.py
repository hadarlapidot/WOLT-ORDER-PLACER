import pytest
import webdriver_manager
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep as sleep

def test_place_order():

    # set up chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # open WOLT website
    driver.get("https://wolt.com/en/discovery")
    
    # look up for Shawarma
    wait = WebDriverWait(driver, 10)


    # search in search bar
    search_bar_locator = (By.CLASS_NAME, 'i131pb3d')
    wait.until(ec.visibility_of_element_located(search_bar_locator))
    search_bar = driver.find_element(*search_bar_locator)
    search_bar.click()
    search_bar.send_keys("Shawarma")
    search_bar.send_keys(Keys.ENTER)

    sleep(3)
