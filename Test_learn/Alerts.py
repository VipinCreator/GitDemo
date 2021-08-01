import time

from selenium import webdriver
alertext="Option3"
driver=webdriver.Chrome(executable_path="F:\Crome\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_xpath("//input[@placeholder='Enter Your Name']").send_keys(alertext)
driver.find_element_by_id("alertbtn").click()

alert=driver.switch_to.alert
val=alert.text
alert.accept()
assert alertext in val

driver.find_element_by_xpath("//input[@placeholder='Enter Your Name']").send_keys(alertext)
driver.find_element_by_id("confirmbtn").click()
time.sleep(5)
alert=driver.switch_to.alert
alert.dismiss()
