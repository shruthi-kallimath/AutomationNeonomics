import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from testCases.conftest import *
from allure_commons.types import AttachmentType


class Test_Signin:

    def test_login(self,url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.login = Login(self.driver)
        self.login.setUserName(ReadConfig.get_username())
        self.login.setPassWord(ReadConfig.get_password())
        self.login.clickSignin()
        return self.driver.page_source
        allure.attach(self.driver.get_screenshot_as_png(),name="TestLoginScreen",attachment_type=AttachmentType.PNG)







