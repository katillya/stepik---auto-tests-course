import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
time.sleep(1)

try:
    driver.get("http://suninjuly.github.io/selects1.html")
    # Initial declaration of the integer res equal to zero
    res = 0
    first_number = driver.find_element_by_id("num1")   # Read first number
    second_number = driver.find_element_by_id("num2")  # Read second number
    first = first_number.text     # Convert first number to string
    second = second_number.text   # Convert second number to string
    res = (int(first) + int(second))   # Get sum of two numbers converted to integers

    vis = str(res)   # Converting integer sum to string value
    sel = Select(driver.find_element_by_id("dropdown"))   # Find the dropdown on the page

    sel.select_by_visible_text(vis)   # Select the right menu item from the dropbox

    # Find the Submit button and click on it
    submit = driver.find_element_by_class_name("btn")
    submit.click()

finally:
    time.sleep(15)
    driver.quit()
