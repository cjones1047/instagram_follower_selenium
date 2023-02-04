import dotenv
import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

SEARCH_WORD = "Python"


class InstaFollower:

    def __init__(self):
        dotenv.load_dotenv()
        self.ig_username = os.getenv("IG_USERNAME")
        self.ig_password = os.getenv("IG_PASSWORD")
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.account_name_list = None

    def login(self):
        ig_login_url = "https://www.instagram.com/"
        self.driver.get(ig_login_url)
        time.sleep(5)
        username_input_el = self.driver.find_element(by=By.NAME, value="username")
        username_input_el.click()
        username_input_el.send_keys(self.ig_username, Keys.TAB, self.ig_password, Keys.ENTER)

    def find_followers(self):
        followers_found = False
        while not followers_found:
            try:
                search_button_el = self.driver.find_element(by=By.CSS_SELECTOR, value='svg[aria-label="Search"]')
            except NoSuchElementException:
                pass
            else:
                search_button_el.click()
                time.sleep(1)
                search_field_el = self.driver.find_element(by=By.CSS_SELECTOR, value='input[aria-label="Search input"]')
                search_field_el.click()
                search_field_el.send_keys(SEARCH_WORD)
                time.sleep(1)
                account_name_els_list = self.driver.find_elements(by=By.CSS_SELECTOR, value='div[class="_aacl _aaco '
                                                                                            '_aacw _aacx _aad6"]')
                self.account_name_list = [account.text for account in account_name_els_list[:10]
                                          if len(account.text) > 0]
                followers_found = True

    def follow(self):
        for account in self.account_name_list:
            account_is_hashtag = False
            if account[0] == "#":
                account_url = f"https://www.instagram.com/explore/tags/{account[1:]}/?next=%2F"
                account_is_hashtag = True
            else:
                account_url = f"https://www.instagram.com/{account}/?next=%2F"
            self.driver.get(account_url)
            account_followed = False
            if account_is_hashtag:
                while not account_followed:
                    # if hashtag HAS been followed
                    try:
                        self.driver.find_element(by=By.CSS_SELECTOR,
                                                 value='button[class="_acan _acap _acaq _acat _aj1-"]')
                    except NoSuchElementException:
                        pass
                    else:
                        break

                    # if hashtag has NOT been followed
                    try:
                        follow_hashtag_button_el = self.driver.find_element(by=By.CSS_SELECTOR,
                                                                            value='button[class="_acan '
                                                                                  '_acap _acaq _acas '
                                                                                  '_aj1-"]')
                    except NoSuchElementException:
                        pass
                    else:
                        follow_hashtag_button_el.click()
                        account_followed = True

            else:
                while not account_followed:
                    # if account HAS been followed
                    try:
                        self.driver.find_element(by=By.CSS_SELECTOR, value='button[class="_acan _acap _acat _aj1-"]')
                    except NoSuchElementException:
                        pass
                    else:
                        break

                    # if account has NOT been followed
                    try:
                        follow_button_el = self.driver.find_element(by=By.CSS_SELECTOR,
                                                                    value='button[class="_acan _acap '
                                                                          '_acas _aj1-"]')
                    except NoSuchElementException:
                        pass
                    else:
                        follow_button_el.click()
                        account_followed = True
