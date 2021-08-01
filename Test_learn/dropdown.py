import time

from selenium import webdriver
ans ="Delhi, India"
driver=webdriver.Chrome(executable_path="F:\Crome\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.find_element_by_xpath("//input[@id='fromCity']").click()

driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
time.sleep(2)
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(cities))
for city in cities:
    if city.text == ans:
        city.click()
        break
driver.find_element_by_xpath("//p[text()='Mumbai, India']").click()
