import shopify
from values import*
from auth_functions import*
import urllib3
from urllib.parse import urlparse, parse_qs
from selenium import webdriver

state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
shopify.Session.setup(api_key=client_id, secret=client_secret)
session = shopify.Session("socalization.myshopify.com", '2024-01')
url = getauthcodeurl(session,state)


# Path to the WebDriver executable
webdriver_path = '/chromedriver'

# Start the WebDriver instance
driver = webdriver.Chrome()
driver.get(url)

LoginShopify(driver)
time.sleep(10)

updated_url=driver.current_url

parsed_url = urlparse(updated_url)

# Get the query parameters as a dictionary
query_params = {key: values[0] for key, values in parse_qs(parsed_url.query).items()}
print(query_params)

access_token = authcode_for_accesstoken(session,query_params)
print(access_token)