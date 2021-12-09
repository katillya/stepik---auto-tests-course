import time
from selenium import webdriver
import math

driver = webdriver.Chrome()
time.sleep(1)

try:
    driver.get("http://suninjuly.github.io/math.html")

    people_radio = driver.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print(people_checked)
    assert people_checked is not None, "People radio is not selected by default"
#    assert people_checked == "false", "People radio is selected by default"

    robots_radio = driver.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

finally:
    time.sleep(15)
    driver.quit()
