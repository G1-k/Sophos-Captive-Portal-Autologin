import sys
from selenium import webdriver


driver = webdriver.Firefox()

try: 
	driver.get("replace_with_captive_portal_link")
except:
	sys.exit(0)

username = driver.find_element_by_name("username")
username.clear()

password = driver.find_element_by_name("password")
password.clear()

username.send_keys("replace_with_credential_username")
password.send_keys("replace_with_password")

driver.find_element_by_id("loginbutton").click()

print ("Logged In.")

driver.close()