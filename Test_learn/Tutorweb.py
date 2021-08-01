from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="F:\Crome\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
#driver.find_elements_by_xpath("//input[@value='radio1']/input")
drop=Select(driver.find_element_by_id("dropdown-class-example"))
drop.select_by_index(1)

#Example showing dynamically selecting check boxes
checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
for check in checkboxes:
    check.click()
    #to check if checkboxes are successfully selected or not
    assert check.is_selected()
    if check.get_attribute("value")== 'option2':
        check.click()
radio=driver.find_elements_by_xpath("//input[@name='radioButton']")
radio[2].click()
driver.find_element_by_css_selector("input[placeholder='Type to Select Countries']").send_keys("India")


