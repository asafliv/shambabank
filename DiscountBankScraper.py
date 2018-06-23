import os
import time

from DataSourceScraper import DataSourceScraper
from selenium import webdriver

class DiscountBankScrape(DataSourceScraper):

    def login(self):
        chrome_path = os.getcwd()+'/chromedriver'
        driver = webdriver.Chrome(executable_path=chrome_path)
        driver.get('https://start.telebank.co.il/apollo/core/templates/lobby/masterPage.html#/LOGIN_PAGE')
        time.sleep(5)
        username = driver.find_element_by_id("tzId")
        password = driver.find_element_by_id("tzPassword")
        aidnum = driver.find_element_by_id("aidnum")

        username.send_keys(os.environ.get("ID"))
        password.send_keys(os.environ.get("password"))
        aidnum.send_keys(os.environ.get("identity_code"))


        driver.find_element_by_class_name('sendBtn').click()
        print driver.current_url
        pass


def main():
    x = DiscountBankScrape()
    x.login()


if __name__ == "__main__":
    main()