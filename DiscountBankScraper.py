import os
import time


from DataSourceScraper import DataSourceScraper
from selenium import webdriver
from requests.utils import dict_from_cookiejar
import cookielib
import datetime
import requests
import urllib
import json


class DiscountBankScrape(DataSourceScraper):
    BASE_URL = 'https://start.telebank.co.il'
    LOGIN_URL = BASE_URL + '/apollo/core/templates/lobby/masterPage.html#/LOGIN_PAGE'
    LAST_TRANASACTIONS_ENDPOINT = BASE_URL + '/Titan/gatewayAPI/lastTransactions/{bank_account}/ByDate'

    def __init__(self):
        self._cookie_policy = cookielib.DefaultCookiePolicy()
        self.cj = cookielib.CookieJar(self._cookie_policy)
        self.session = requests.session()
        self.driver = None

    def login(self):
        chrome_path = os.getcwd()+'/chromedriver'
        self.driver = webdriver.Chrome(executable_path=chrome_path)
        self.driver.get(self.LOGIN_URL)
        time.sleep(5)
        self.set_selenium_param("tzId", os.environ.get("ID"))
        self.set_selenium_param("tzPassword", os.environ.get("password"))
        self.set_selenium_param("aidnum", os.environ.get("identity_code"))
        self.driver.find_element_by_class_name('sendBtn').click()

    def set_selenium_param(self, input_id, input_value):
        input = self.driver.find_element_by_id(input_id)
        input.send_keys(input_value)

    def pull(self):
        # print self.driver.current_url
        time.sleep(5)
        expiration_time = (datetime.datetime.now() + datetime.timedelta(days=2)).strftime('%s')
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            c = cookielib.Cookie(version=0, name=cookie['name'], value=cookie['value'], port=None, port_specified=False,
                                 domain=cookie['domain'],
                                 domain_specified=True, domain_initial_dot=True, path=cookie['path'], path_specified=True,
                                 secure=cookie['secure'],
                                 expires=expiration_time, discard=False, comment=None, comment_url=None, rest={},
                                 rfc2109=False)
            self.cj.set_cookie(c)
        url = self.LAST_TRANASACTIONS_ENDPOINT.format(bank_account='0014703124')
        params = {'IsCategoryDescCode': True,
                  'IsTransactionDetails': True,
                  'IsEventNames': True,
                  'FromDate': '20180323',
                  'ToDate': '20180624',
                  'FromAmount': '0',
                  'ToAmount': '999999999999.99'
                  }
        full_url = url + "?" + urllib.urlencode(params)
        resp = requests.get(full_url, cookies=dict_from_cookiejar(self.cj))
        data = json.loads(resp.content)
        for key, val in data[u'CurrentAccountLastTransactions'][u'OperationEntry'][4].iteritems():
            print '%s: %s' % (key, val)
        print 'fuck Yeah!'


def main():
    x = DiscountBankScrape()
    x.login()
    x.pull()


if __name__ == "__main__":
    main()
