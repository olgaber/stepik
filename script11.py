from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_name("firstname")
    lastname = browser.find_element_by_name("lastname")
    email = browser.find_element_by_name("email")
    choose_btn = browser.find_element_by_id("file")
    submit_btn = browser.find_element_by_css_selector("button")

    name.send_keys("1")
    lastname.send_keys("1")
    email.send_keys("1")

    choose_btn.send_keys("/home/olga/environments/selenium_env/selenium_course/test.txt")
    submit_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
