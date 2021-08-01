from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//input[@type='search']")
    proBut = (By.XPATH, "//div[@class='products']/div")

    def shopItem(self):
        return self.driver.find_element(*Homepage.shop)

    def productSelect(self):
        return self.driver.find_element(*Homepage.proBut)
