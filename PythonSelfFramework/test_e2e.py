



import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Baseclass import Baseclass
from Home import Homepage


class Testone(Baseclass):
    def test_e2e(self):
        list1 = []
        list2 = []
        #from selenium.webdriver.support.wait import expected_conditions
       #driver=webdriver.Chrome(executable_path="F:\Crome\chromedriver.exe")
       #driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        #driver.implicitly_wait(5)   #implicit wait
        homepage = Homepage(self.driver)
        homepage.shopItem().send_keys("ber")
        time.sleep(2)
        count1 = len(self.driver.find_elements_by_xpath("//div[@class='products']/div"))

        print(count1)

        assert count1 == 3

        items=self.driver.find_elements_by_xpath("//div[@class='product-action']/button")

        for item in items:
            list1.append(item.find_element_by_xpath("parent::div/parent::div/h4").text)
            item.click()


        self.driver.find_element_by_xpath("//img[@alt='Cart']").click()
        self.driver.find_element_by_xpath("//div[@class='action-block']/button").click()

        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
        veggies = self.driver.find_elements_by_css_selector("p.product-name")
        for veg in veggies:
            list2.append(veg.text)
        amt1 = self.driver.find_element_by_css_selector("span.discountAmt").text
        self.driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector(".promoBtn").click()
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
        print(self.driver.find_element_by_css_selector("span.promoInfo").text)
        amt2 = self.driver.find_element_by_css_selector("span.discountAmt").text

        #driver.close()
        print(list1)
        print(list2)
        assert list1 == list2
        print(amt1)
        print(amt2)
        assert float(amt2) < int(amt1)

        amounts= self.driver.find_elements_by_xpath("//tr/td[5]/p")
        sum=0
        for amount in amounts:
          sum =sum + int(amount.text)
        print(sum)

        total=self.driver.find_element_by_css_selector("span[class='totAmt']")

        assert sum == int(total.text)