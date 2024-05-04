import shopify
import binascii
import os
import time
from values import*
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

elementEmailLogin = "//input[@type='email']"
elementLoginContinue = "//span[text()='Continue with email']"
elementPasswordLogin = "//input[@label='Password']"
elementLoginButton = "//span[@class='ui-button__text']"
EMAIL_ACCOUNT = "intern@socalization.com"
PASSWORD = "idbWHdvm"

def getauthcodeurl(session,state):
    shopify.Session.setup(api_key=client_id, secret=client_secret)
    auth_url = session.create_permission_url(['read_products','read_orders', 'read_all_orders','read_inventory'], 'https://www.socalization.com/',state)
    return auth_url

def authcode_for_accesstoken(session,request_params):
    access_token = session.request_token(request_params)
    return access_token

def Selenium_ElementSelectXPath(XPath,driver):
    element= driver.find_element(By.XPATH, XPath)
    return element

def LoginShopify(driver):
    Selenium_ElementSelectXPath(XPath=elementEmailLogin, driver=driver).send_keys(EMAIL_ACCOUNT)
    time.sleep(2)

    Selenium_ElementSelectXPath(XPath=elementLoginContinue, driver=driver).click()
    time.sleep(2)
    #For CAPTCHA
    #Selenium_ElementSelectXPath(XPath=elementEmailLogin, driver=driver).send_keys(EMAIL_ACCOUNT)
    #time.sleep(30)

    Selenium_ElementSelectXPath(XPath=elementPasswordLogin, driver=driver).send_keys(PASSWORD)
    time.sleep(2)
    Selenium_ElementSelectXPath(XPath=elementLoginButton, driver=driver).click()
    print("Logged into Socalization Shopify!")


