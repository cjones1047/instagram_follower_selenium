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
        ig_username = os.getenv("IG_USERNAME")
        ig_password = os.getenv("IG_PASSWORD")
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        ig_login_url = "https://www.instagram.com/accounts/login/"
        self.driver.get(ig_login_url)
        time.sleep(1)

    def find_followers(self):
        pass

    def follow(self):
        pass
