from selenium import webdriver
import time
"""
	This test will fail because the element appears 
	on the page with a delay
"""
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

time.sleep(10)
browser.quit()