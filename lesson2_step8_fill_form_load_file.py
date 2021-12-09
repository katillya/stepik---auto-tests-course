from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
value1 = "input:nth-child(2)"
value2 = "input:nth-child(4)"
value3 = "input:nth-child(6)"
value4 = "btn"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    browser.find_element_by_css_selector(value1).send_keys("Ivan")

    browser.find_element_by_css_selector(value2).send_keys("Petrov")

    browser.find_element_by_css_selector(value3).send_keys("blah@blah.com")

    browser.find_element_by_id("file").send_keys(file_path)

    browser.find_element_by_class_name(value4).click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# И не забываем оставить пустую строку в конце файла