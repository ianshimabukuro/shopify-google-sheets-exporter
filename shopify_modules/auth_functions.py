import shopify
import time
from ids_passwords_strings.values import*
from selenium.webdriver.common.by import By

elementEmailLogin = "//input[@type='email']"
elementLoginContinue = "//span[text()='Continue with email']"
elementPasswordLogin = "//input[@label='Password']"
elementLoginButton = "//span[@class='ui-button__text']"
EMAIL_ACCOUNT = "intern@socalization.com"
PASSWORD = "idbWHdvm"

#Shopify code url
def getauthcodeurl(session,state):
    shopify.Session.setup(api_key=client_id, secret=client_secret)
    auth_url = session.create_permission_url(['read_products','read_orders', 'read_all_orders','read_inventory'], 'https://www.socalization.com/',state)
    return auth_url

#Exchange Auth code in the Auth url for an Access Token
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


