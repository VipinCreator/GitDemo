import pytest

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="F:\Crome\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    request.cls.driver = driver
