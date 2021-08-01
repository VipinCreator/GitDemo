from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\Crome\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()
newwindow=driver.window_handles[1]
driver.switch_to.window(newwindow)
print(driver.find_element_by_tag_name("h3").text)

#Frames
