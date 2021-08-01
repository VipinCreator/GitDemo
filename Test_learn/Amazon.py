from selenium import webdriver

driver=webdriver.Chrome(executable_path="F:\Crome\chromedriver.exe")
driver.get("https://www.amazon.com")
driver.maximize_window()
element=driver.find_element_by_id("nav-link-accountList")
element.click()
driver.implicitly_wait(1000)
driver.find_element_by_css_selector("input[name='email']").send_keys("vipinpillai84@gmail.com")

driver.find_element_by_xpath("//input[@id='continue']").click()
print(driver.find_element_by_class_name("a-spacing-small").text)

driver.find_element_by_link_text("Forgot your password?").click()
driver.find_element_by_xpath("//input[@type='hidden']/h1")