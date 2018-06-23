import os
from DataSourceScraper import DataSourceScraper
from selenium import webdriver

class DiscountBankScrape(DataSourceScraper):

    def login(self):
        chrome_path = os.getcwd()+'/chromedriver'
        driver = webdriver.Chrome(executable_path=chrome_path)
        driver.get('https://www.discountbank.co.il/DB/private')
        pass


def main():
    x = DiscountBankScrape()
    x.login()


if __name__ == "__main__":
    main()

print "Guru99"
