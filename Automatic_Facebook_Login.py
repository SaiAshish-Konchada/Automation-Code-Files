# importing the required module
from selenium import webdriver

# store the credentials
user_id = "email_or_phone_number_to_your_facebook_account"
password = "password_to_your_facebook_account"

# gain object from webdriver and visit facebook.com
browser= webdriver.Chrome('path_to_chromedriver.exe_file_we_downloaded_earlier')
browser.get('https://www.facebook.com/')

# find the email input and send the email or phone credential
user_box = browser.find_element_by_id("email")  # For detecting the user id box
user_box.send_keys(user_id)                     # Enter the user id in the box

# send the password
password_box = browser.find_element_by_id("pass")   # For detecting the password box
password_box.send_keys(password)                    # For detecting the password in the box

# click the login
login_box = browser.find_element_by_name("login")  # For detecting the Login button
login_box.click()
