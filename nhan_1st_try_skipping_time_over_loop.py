import pandas as pd
# import web driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys #  [Keys.LEFT, Keys.DOWN, Keys.RIGHT, Keys.UP]
from parsel import Selector
from shutil import which
from time import sleep
import time
 
class LinkedIn_URL:
    '''
    get linked in URL by using outlook
    '''
    def __init__(self, url):
        # specifies the path to the chromedriver.exe
        self.driver = webdriver.Chrome(executable_path=which("chromedriver"))
        self.driver.get(url)
    
    def get_site_info(self):
        # get the site information
        print('URL:', self.driver.current_url)
        print('Title:', self.driver.title)
        sleep(2)
        self.driver.save_screenshot('screen_shot.png')

    def outlook_signin(self, username, password):
        # sign in website
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

    def linked_in_signin(self, username, password):
        # Save current_window as the main_window
        main_window = self.driver.current_window_handle
        # Open new-tab
        self.driver.execute_script("window.open();")
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.get('https://www.linkedin.com')
        sleep(2)

        # Log-in Linkedin in the second TAB
        username = self.driver.find_element_by_name('session_key')
        username.send_keys(username)
        password = self.driver.find_element_by_name('session_password')
        password.send_keys(password)
        self.class_name_click('sign-in-form__submit-button')
        sleep(1)

        # Switch back to main window
        self.driver.switch_to_window(main_window)
        sleep(1)

    def get_url(self, email_list):
        # choose people contact
        self.selector_click('#app > div > div._3KAPMPOz8KsW24ooeUflK2 > div > div._1TpU2KF6f_EeQiytBaYj8I > div._25oA4qBLP_b6P080cw5s2H.css-43 > div._1_iewjAgd8BRIHH3zHMH1V > div > div > div:nth-child(3) > div > a > span')
        ## loop though contact list
        # select first contact
        self.selector_click('#HubPersonaId_AQQkADAwATNiZmYAZC0zMwBkYS1jNDQANS0wMAItMDAKABAA\/0L4nPVSf0WielUcdLGSkw\=\= > div > div._3qxq4FbPD_ovy_o1o8-N4E')
        # select LinkedIn button
        self.xpath_click('/html/body/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/button[4]')
        # Loop email over email_contact
        linkedin_url = []
        search_query = self.driver.find_element_by_xpath('//*[@id="SearchBox91"]')  ## change each-time you log-in
        for mail in email_list:
            ## Enter & access to search_box of the email_contact
            search_query = self.driver.find_element_by_xpath('//*[@id="SearchBox91"]')
            search_query.send_keys(mail)
            search_query.send_keys(Keys.ENTER)

            ## Find the button of Linkedin-tab by name 
            contact_button = self.driver.find_element_by_xpath('//*[class = "ms-Pivot-text-349 text-354"]')
            contact_button.click()  

            ## Access the button : "See full profile on Linkedin"
            contact_button = self.driver.find_element_by_name("ViewProfileInLinkedIn")
            contact_button.click()  

            ## get the url-link
            link = self.driver.current_url
            linkedin_url.append(link)
        return linkedin_url

    def selector_click(self, css_selector):
        self.driver.find_element_by_css_selector(css_selector).click()

    def xpath_click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
    
    def class_name_click(self, class_name):
        self.driver.find_element_by_class_name(class_name).click()


class Url_Scrap:
    def __init__(self, linked_in_url, url_list):
        # specifies the path to the chromedriver.exe
        self.driver = webdriver.Chrome(executable_path=which("chromedriver"))
        self.driver.get(linked_in_url)
        self.url_list = url_list

    def linked_in_signin(self, username, password):
        # Save current_window as the main_window
        username = self.driver.find_element_by_name('session_key')
        username.send_keys(username)
        password = self.driver.find_element_by_name('session_password')
        password.send_keys(password)
        self.driver.find_element_by_class_name('sign-in-form__submit-button').click()

    def loop_through_links(self):
        ## initialize empty list
        names, jobs, company, education, location, school  = [], [], [], [], [], []
        # **Step 3: finding `xpath`** and using skipping-time
        # For example, you can find the infomation of the `job title` by searching the `inspect` then copy its `full xpath`
        ## append the obtained values from Selector function
        T0 = time.time()
        for k in range(len(self.url_list)):
            t0 = time.time()
            path = self.url_list[k]
            self.driver.get(path)
            sel = Selector(text=self.driver.page_source)     
            names.append(sel.xpath("/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]/text()").extract_first())
            jobs.append( sel.xpath("/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/h2/text()").extract_first() )
            company.append(sel.xpath('/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[2]/ul/li[1]/a/span/text()').extract_first())
            education.append(sel.xpath('/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[2]/section/ul/li[1]/div/div/a/div[2]/div/p[1]/span[2]/text()').extract_first())
            location.append(sel.xpath('/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[2]/li[1]/text()').extract_first())
            school.append(sel.xpath('/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[2]/section/ul/li[1]/div/div/a/div[2]/div/h3/text()').extract_first())
            print("step = %s, appending complete after %s (seconds) "%(k, time.time() - t0))
            # waiting
            if (k+1) % 10 == 0:
                sleep(5)

        ## Step 4. Create dataframe
        
        df = pd.DataFrame({'name': names, 
                        'job title': jobs, 
                        'company': company, 
                        'education': education, 
                        'school': school, 
                        'location': location, 
                        'url': self.url_list}) 

        for col in df.columns:
            df[col] = df[col].apply(lambda x : self.remove(x))
        return df
    def remove(self,x):
        if x == None:
            x = None
        else:
            x = x.replace('\n\t', '').replace('\n', '')
        return x


if __name__ == '__main__':
    # load data frame
    df = pd.read_csv("data.csv")
    email_list = df['Email']  ## Noting that df is your loaded-dataframe of "Customer information"
    outlook_account = 'thanosteamk09@gmail.com'
    outlook_password = 'thaNos99*'
    linkedin_account = 'thanosteamk09@gmail.com'
    linkedin_password = 'thaNos99*'
    linked_url = 'https://www.linkedin.com'
    # driver.get method() will navigate to a page given by the URL address
    outlook = LinkedIn_URL('https://outlook.live.com/owa/')
    # outlook.get_site_info()
    outlook.outlook_signin(outlook_account, outlook_password)
    outlook.linked_in_signin(linkedin_account, linkedin_password)
    URL_list = outlook.get_url(email_list)
    # Close driver

    # Scrap from linked in URL
    url_scrap = Url_Scrap(linked_url, URL_list)
    url_scrap.linked_in_signin(linkedin_account, linkedin_password)
    url_scrap.loop_through_links()
    outlook.driver.close()
