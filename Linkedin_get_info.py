# import web driver
from selenium import webdriver

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('C:/Users/Mr.Rocker/AppData/Local/Google/Chrome/Application/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element_by_name('session_key')

# send_keys() to simulate key strokes
username.send_keys('ndkhoa.tth@gmail.com')

# locate password form by_class_name
password = driver.find_element_by_name('session_password')

# send_keys() to simulate key strokes
password.send_keys('MiKa&020617$m')

# locate submit button by_class_name
log_in_button = driver.find_element_by_name('sign-in-form__submit-button')
log_in_button.click()

# locate submit button by_class_id
log_in_button = driver.find_element_by_class_id('login submit-button')

# locate submit button by_xpath
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
log_in_button.click()