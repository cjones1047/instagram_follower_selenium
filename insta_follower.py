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
        # time.sleep(3)
        # try:
        #     avoid_save_info_el = self.driver.find_element(by=By.CSS_SELECTOR, value='button[class="_acan _acao '
        #                                                                             '_acas _aj1-"]')
        #     avoid_save_info_el.click()
        #     time.sleep(1)
        # except NoSuchElementException:
        #     pass
        # try:
        #     avoid_save_info_el = self.driver.find_element(by=By.CSS_SELECTOR, value='span[class="_2iem"]')
        #     avoid_save_info_el.click()
        #     time.sleep(1)
        # except NoSuchElementException:
        #     pass
        # # log_in_button = self.driver.find_element(by=By.CSS_SELECTOR, value='a[href="/accounts/login/?next=%2F&'
        # #                                                                    'source=logged_out_half_sheet"]')
        # # log_in_button.click()
        # # time.sleep(1)
        # # username_input_el = self.driver.find_element(by=By.NAME, value="username")
        # # username_input_el.click()
        # # username_input_el.send_keys(self.ig_username, Keys.TAB, self.ig_password, Keys.ENTER)
        # # time.sleep(1)
        # # avoid_save_info_el = self.driver.find_element(by=By.CSS_SELECTOR, value='button[class="_acan _acao '
        # #                                                                         '_acas _aj1-"]')
        # # avoid_save_info_el.click()
        # # time.sleep(1)
        # avoid_notifications_el = self.driver.find_element(by=By.CSS_SELECTOR, value='button[class="_a9-- _a9_1"]')
        # avoid_notifications_el.click()
        # time.sleep(1)

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
                account_name_els_list = self.driver.find_elements(by=By.CSS_SELECTOR, value='div[class="_aacl _aaco _aacw '
                                                                                            '_aacx _aad6"]')
                self.account_name_list = [account.text for account in account_name_els_list]
                followers_found = True

    def follow(self):
        print(self.account_name_list)
