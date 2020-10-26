# import web driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys #  [Keys.LEFT, Keys.DOWN, Keys.RIGHT, Keys.UP]

from shutil import which
from time import sleep


# # get URL
# select_linked_in = driver.find_elements_by_css_selector("#Pivot204-Tab3 > span > span > span")
# select_linked_in.click()



# #try to get URL of linke tab
# wait_variable = WebDriverWait(driver, 15)
# links = wait_variable.until(expected_conditions.visibility_of_any_elements_located((By.TAG_NAME, "a")))
# print(len(links))
# for link in links:
#     print(link.text)
# wait_variable.until(expected_conditions.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "See full profile on LinkedIn"))).click()


 
 
class Selenium_outlook:
    

    def __init__(self, url):
        # specifies the path to the chromedriver.exe
        self.driver = webdriver.Chrome(executable_path=which("chromedriver"))
        self.driver.get(url)
 
    def get_site_info(self):
        print('URL:', self.driver.current_url)
        print('Title:', self.driver.title)
        sleep(5)
        self.driver.save_screenshot('screen_shot.png')

    def outlook_signin(self, username, password):
        # sign in
        log_in_button = self.driver.find_element_by_css_selector('body > header > div > aside > div > nav > ul > li:nth-child(2) > a')
        log_in_button.click()

        # input email
        username_loc = self.driver.find_element_by_css_selector('#i0116')
        username_loc.send_keys(username)
        username_loc.send_keys(Keys.ENTER)
        sleep(1)

        # input password
        password_loc = self.driver.find_element_by_css_selector('#i0118')
        password_loc.send_keys(password)
        sleep(0.5)
        pass_inter = self.driver.find_element_by_css_selector('#idSIButton9')
        pass_inter.click()

        # Sign in yes button
        stay_sign_in = self.driver.find_element_by_css_selector('#idSIButton9')
        stay_sign_in.click()
        sleep(0.5)

    def contact_loop(self):
        # choose people contact
        people_button = self.driver.find_element_by_css_selector('#app > div > div._3KAPMPOz8KsW24ooeUflK2 > div > div._1TpU2KF6f_EeQiytBaYj8I > div._25oA4qBLP_b6P080cw5s2H.css-43 > div._1_iewjAgd8BRIHH3zHMH1V > div > div > div:nth-child(3) > div > a > span')
        people_button.click()

        ## loop though contact list
        # select first contact
        first_contact = self.driver.find_element_by_css_selector(r'#HubPersonaId_AQQkADAwATNiZmYAZC0zMwBkYS1jNDQANS0wMAItMDAKABAA\/0L4nPVSf0WielUcdLGSkw\=\= > div > div._3qxq4FbPD_ovy_o1o8-N4E')
        first_contact.click()


if __name__ == '__main__':
    outlook_account = 'thanosteamk09@gmail.com'
    outlook_password = 'thaNos99*'
    # driver.get method() will navigate to a page given by the URL address
    outlook = Selenium_outlook('https://outlook.live.com/owa/')
    # outlook.get_site_info()
    outlook.outlook_signin(outlook_account, outlook_password)
    # Close driver
    # outlook.driver.close()