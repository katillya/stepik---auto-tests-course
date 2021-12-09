from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    rent = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    browser.find_element_by_id("book").click()

    text = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, "simple_text"), 'Math is real magic!'))
    
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    
    browser.find_element_by_id("solve").click()


finally:

    time.sleep(15)
    browser.quit()
