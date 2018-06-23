import os
import time

from DataSourceScraper import DataSourceScraper
from selenium import webdriver

class DiscountBankScrape(DataSourceScraper):

    def login(self):
        chrome_path = os.getcwd()+'/chromedriver'
        driver = webdriver.Chrome(executable_path=chrome_path)
        driver.get('https://www.discountbank.co.il/DB/private')
        time.sleep(5)
        driver.get_screenshot_as_file("asaf")
        driver.find_element_by_class_name('retail-log-in-button').click()
        print driver.current_url
        pass


def main():
    x = DiscountBankScrape()
    x.login()


if __name__ == "__main__":
    main()