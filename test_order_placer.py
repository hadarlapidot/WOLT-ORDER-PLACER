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
from flask import Flask, render_template, request
from page_objects.base_page import BasePage

app = Flask(__name__)
driver = None

@app.before_request
def setup_driver():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
@app.teardown_appcontext
def teardown_driver(exception=None):
    global driver
    if driver:
        driver.quit()

# Display the form
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission

@app.route('/submit', methods=['POST'])
def test_place_order():
    global driver
    # The food to be ordered
    order = request.form['order'] 

    # open WOLT website
    driver.get("https://wolt.com/en/discovery")
    
    # Instantiate a basePage object
    page = BasePage(driver)
    wait = WebDriverWait(driver, 10)


    # First: sign in
    # If signed out then sign in. Else: sign in.
    # if page.is_logged_in():
    #     page.log_in()
    # else:
    #     driver.quit()




    # look up for Pizza


    # search in search bar
    search_bar_locator = (By.CLASS_NAME, 'i131pb3d')
    wait.until(ec.visibility_of_element_located(search_bar_locator))
    search_bar = driver.find_element(*search_bar_locator)
    search_bar.click()
    search_bar.send_keys(order)
    search_bar.send_keys(Keys.ENTER)

    sleep(5)
