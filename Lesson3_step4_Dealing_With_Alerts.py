from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

#   Pressing button "I want to go on a magical journey!
    browser.find_element_by_class_name("btn-primary").click()

    alert = browser.switch_to.alert   # Switching to the alert modal popup
    alert.accept()                    # Accepting (confirming) the alert's question

#   Reading the numeric value after the formula
    x = browser.find_element_by_id("input_value").text
    y = calc(x)                       # Sending the gotten value to the calc function

#   Entering the calculated variable into the text box
    browser.find_element_by_id("answer").send_keys(y)

#   Submitting the answer
    browser.find_element_by_css_selector("[type='submit']").click()


finally:
    time.sleep(20)
    browser.quit()
