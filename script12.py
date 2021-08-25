from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element_by_css_selector("button[type='submit']")
    btn.click()
    alert = browser.switch_to.alert
    alert.accept()

    x = int(browser.find_element_by_id("input_value").text)
    result = calc(x)

    browser.find_element_by_id("answer").send_keys(result)
    btn1 = browser.find_element_by_css_selector("button[type='submit']")
    btn1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
