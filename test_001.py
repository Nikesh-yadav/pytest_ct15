from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_credence001:
    def test_sum01(self):
        a=10
        b=15
        sum=a+b
        print(sum)
        if sum == 25:
            assert True
        else:
            assert False


    def test_credkart_02(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title ==('Credence'):
            assert True
        else:
            assert False


















