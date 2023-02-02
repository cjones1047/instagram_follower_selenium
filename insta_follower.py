import dotenv
import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class InstaFollower:

    def __init__(self):
        dotenv.load_dotenv()
        self.ig_username = os.getenv("IG_USERNAME")
        self.ig_password = os.getenv("IG_PASSWORD")
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        ig_login_url = "https://www.instagram.com/"
        self.driver.get(ig_login_url)
        time.sleep(1)
        username_input_el = self.driver.find_element(by=By.NAME, value="username")
        username_input_el.click()
        username_input_el.send_keys(self.ig_username, Keys.TAB, self.ig_password, Keys.ENTER)
        time.sleep(3)
        try:
            avoid_save_info_el = self.driver.find_element(by=By.CSS_SELECTOR, value='button[class="_acan _acao '
                                                                                    '_acas _aj1-"]')
            avoid_save_info_el.click()
            time.sleep(1)
        except NoSuchElementException:
            pass
        try:
            avoid_save_info_el = self.driver.find_element(by=By.CSS_SELECTOR, value='span[class="_2iem"]')
            avoid_save_info_el.click()
            time.sleep(1)
        except NoSuchElementException:
            pass
        # log_in_button = self.driver.find_element(by=By.CSS_SELECTOR, value='a[href="/accounts/login/?next=%2F&'
        #                                                                    'source=logged_out_half_sheet"]')
        # log_in_button.click()
        # time.sleep(1)
        # username_input_el = self.driver.find_element(by=By.NAME, value="username")
        # username_input_el.click()
        # username_input_el.send_keys(self.ig_username, Keys.TAB, self.ig_password, Keys.ENTER)
        # time.sleep(1)
        # avoid_save_info_el = self.driver.find_element(by=By.CSS_SELECTOR, value='button[class="_acan _acao '
        #                                                                         '_acas _aj1-"]')
        # avoid_save_info_el.click()
        # time.sleep(1)
        avoid_notifications_el = self.driver.find_element(by=By.CSS_SELECTOR, value='button[class="_a9-- _a9_1"]')
        avoid_notifications_el.click()
        time.sleep(1)

    def find_followers(self):
        pass

    def follow(self):
        pass
