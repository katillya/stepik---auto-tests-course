import time
from selenium import webdriver
import math

driver = webdriver.Chrome()
time.sleep(1)

# Constructing separate function calc to calculate the value
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver.get("http://suninjuly.github.io/math.html")

    x_element = driver.find_element_by_id("input_value")
    x = x_element.text

    check = driver.find_element_by_id("robotCheckbox").click()
    #check.click() - using more compact form in the previous operation

    radio = driver.find_element_by_css_selector("[value='robots']").click()
    #radio.click() - using more compact form in the previous operation

    y = calc(x)      # Calling the calc function

    input = driver.find_element_by_id("answer")
    input.send_keys(y)

    time.sleep(5)
    submit = driver.find_element_by_css_selector("[type='submit']").click()

finally:
    time.sleep(15)
    driver.quit()
