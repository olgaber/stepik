from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_obj = browser.find_element_by_id("treasure")
    val = treasure_obj.get_attribute("valuex")

    result = calc(val)
    el1 = browser.find_element_by_id("answer")
    el1.send_keys(result)

    e12 = browser.find_element_by_id("robotCheckbox").click()

    el3 = browser.find_element_by_id("robotsRule").click()

    el4 = browser.find_element_by_css_selector("button[type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

