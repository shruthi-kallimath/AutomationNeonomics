from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Login:
    textbox_username_id="username"
    textbox_password_id="password"
    button_signin_id="kc-login"

    def __init__(self,driver):
        self.driver=driver


    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassWord(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickSignin(self,):
        self.driver.find_element(By.ID,self.button_signin_id).click()