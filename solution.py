from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

import time

import math

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    
    #time.sleep(1)
    
    x1 = browser.find_element(By.ID, "num1").text  
    
    print(x1)
    
    x2 = browser.find_element(By.ID, "num2").text
    
    print(x2)
    
    y = int(x1) + int(x2)
    
    print(y)
    
    select.select_by_value(str(y)) # ищем элемент
    
    time.sleep(1)
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
