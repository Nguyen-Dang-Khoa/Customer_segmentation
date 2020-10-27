# import web driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys #  [Keys.LEFT, Keys.DOWN, Keys.RIGHT, Keys.UP]

from shutil import which
from time import sleep
 
class Selenium_outlook:
    '''
    get linked in URL by using outlook
    '''
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
        self.selector_click('body > header > div > aside > div > nav > ul > li:nth-child(2) > a')

        # input email
        username_loc = self.driver.find_element_by_css_selector('#i0116')
        username_loc.send_keys(username)
        username_loc.send_keys(Keys.ENTER)
        sleep(1)

        # input password
        password_loc = self.driver.find_element_by_css_selector('#i0118')
        password_loc.send_keys(password)
        sleep(0.5)
        self.selector_click('#idSIButton9')

        # Sign in yes button
        self.selector_click('#idSIButton9')
        sleep(0.5)

    def contact_loop(self):
        # choose people contact
        self.selector_click('#app > div > div._3KAPMPOz8KsW24ooeUflK2 > div > div._1TpU2KF6f_EeQiytBaYj8I > div._25oA4qBLP_b6P080cw5s2H.css-43 > div._1_iewjAgd8BRIHH3zHMH1V > div > div > div:nth-child(3) > div > a > span')
        ## loop though contact list
        # select first contact
        self.selector_click('#HubPersonaId_AQQkADAwATNiZmYAZC0zMwBkYS1jNDQANS0wMAItMDAKABAA\/0L4nPVSf0WielUcdLGSkw\=\= > div > div._3qxq4FbPD_ovy_o1o8-N4E')
        # select LinkedIn button
        self.xpath_click('/html/body/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/button[4]')


    def selector_click(self, css_selector):
        self.driver.find_element_by_css_selector(css_selector).click()

    def xpath_click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()



if __name__ == '__main__':
    outlook_account = 'thanosteamk09@gmail.com'
    outlook_password = 'thaNos99*'
    # driver.get method() will navigate to a page given by the URL address
    outlook = Selenium_outlook('https://outlook.live.com/owa/')
    # outlook.get_site_info()
    outlook.outlook_signin(outlook_account, outlook_password)
    outlook.contact_loop()
    # Close driver
    outlook.driver.close()
