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
from flask import Flask, render_template, request, redirect, flash, url_for
from page_objects.base_page import BasePage
from selenium.common.exceptions import TimeoutException
import flask
from selenium.webdriver.common.action_chains import ActionChains


app = Flask(__name__)
app.secret_key = 'supersecretkey'
driver = None

@app.before_request
def setup_driver():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()


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

@app.route('/submit', methods=['GET','POST'])
def test_place_order():
    global driver
    # The food category to be ordered
    food_category = request.form['food_category'] 

    # open WOLT website
    driver.get("https://wolt.com/en/discovery")
    
    
    # Instantiate a basePage object
    page = BasePage(driver)
    wait = WebDriverWait(driver, 3)


    # First: sign in
    # If signed out then sign in. Else: sign in.
    # if page.is_logged_in():
    #     page.log_in()
    # else:
    #     driver.quit()

    # search in search bar
    search_bar_locator = (By.CLASS_NAME, 'i131pb3d')
    wait.until(ec.visibility_of_element_located(search_bar_locator))
    search_bar = driver.find_element(*search_bar_locator)
    search_bar.click()
    search_bar.send_keys(food_category)
    search_bar.send_keys(Keys.ENTER)

    sleep(2)

    # if there are no results, go back to home page
    try:
        driver.find_element(By.CSS_SELECTOR, 'h1.tseoo83')
        flash(f"Sorry, no results for: {food_category}.", 'error')
        return redirect(location='http://127.0.0.1:5000/')
    except ec.NoSuchElementException:
        pass
    
    # now search for the specific restaurant, If it doesn't exist, go back to homepage. 
    # If it exists, click it
    restaurant_name = request.form['restaurant'] 
    try:
        restaurant_locator = (By.LINK_TEXT, restaurant_name)
        wait.until(ec.element_to_be_clickable(restaurant_locator))
        restaurant_element = driver.find_element(*restaurant_locator)
        restaurant_element.click()
        sleep(2)
    except TimeoutException:
        sleep(3)
        flash(f"Sorry, {restaurant_name} doesn't seem to exist. Please try to enter a different restaurant", 'error')
        return redirect(location='http://127.0.0.1:5000/')

    # # add the order to the cart
    # # 1. locate the dish
    
    # $$$$$$$$$ TRIAL $$$$$$$$$$
    try:        
        # Locate the element you want to interact with
        order_locator = (By.XPATH, "//div//h3[contains(text(), 'דיל זוגי')]")
        element = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable(order_locator)
        )

        # Use JavaScript to click the element
        driver.execute_script("arguments[0].scrollIntoView();", element)  # Ensure element is in view
        driver.execute_script("arguments[0].click();", element)  # Click element using JS

        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "s1vlpcg2")))
        sleep(5)
    except TimeoutException:
        return "It didn't work.. again..."
    # $$$$$$$$$ TRIAL $$$$$$$$$$

    flash(message='Order successfully placed', category='success')
    return redirect(location='http://127.0.0.1:5000/')