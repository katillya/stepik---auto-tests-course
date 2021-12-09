import time
from selenium import webdriver
import math

driver = webdriver.Chrome()
time.sleep(1)

# Constructing separate function calc to calculate the value
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver.get("http://suninjuly.github.io/execute_script.html")

    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    print(x)

    y = calc(x)      # Calling the calc function

    input = driver.find_element_by_id("answer")
    input.send_keys(y)

    check = driver.find_element_by_id("robotCheckbox").click()
    radio = driver.find_element_by_css_selector("[value='robots']")
    button = driver.find_element_by_tag_name("button")

    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    radio.click()

    time.sleep(2)
    button.click()

finally:
    time.sleep(15)
    driver.quit()
