#To hover over an element and click
from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="F:\Crome\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/hovers")

action = ActionChains(driver)

action.move_to_element(driver.find_element_by_xpath("//img[@alt='User Avatar']")).perform()
action.move_to_element(driver.find_element_by_link_text("View profile")).click().perform()