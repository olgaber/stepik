from selenium import webdriver
import time
#import math
from selenium.webdriver.support.ui import Select

def calc(x, y):
  return str(x + y)

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el1 = int(browser.find_element_by_id("num1").text)
    el2 = int(browser.find_element_by_id("num2").text)
    
    #print(el1_txt)
    #print(el2_txt)

    result = calc(el1, el2)
    print(result)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(result) # ищем элемент с текстом "Python"

    browser.find_element_by_css_selector("button.btn").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

