from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    result = calc(x)
    el1 = browser.find_element_by_id("answer")
    el1.send_keys(result)

    e12 = browser.find_element_by_css_selector("label[for='robotCheckbox']").click()

    el3 = browser.find_element_by_css_selector("label[for='robotsRule']").click()

    el4 = browser.find_element_by_css_selector("button[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
