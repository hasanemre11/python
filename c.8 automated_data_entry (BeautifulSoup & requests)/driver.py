from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://docs.google.com/forms/d/e/1FAIpQLSc2ZX_mvx0TwzPqxqZpY54lgDExt2re3FA6pxqdw-fGphLd0g/viewform"


class Driver:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        self.address = self.driver.find_element(By.XPATH,
                                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                                '1]/div/div[1]/input')
        self.price = self.driver.find_element(By.XPATH,
                                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                              '1]/div/div[1]/input')
        self.link = self.driver.find_element(By.XPATH,
                                             '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                             '1]/div/div[1]/input')
        self.button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    def send_data(self, a, p, m):
        time.sleep(2)
        self.address.send_keys(a)
        self.price.send_keys(p)
        self.link.send_keys(m)
        self.button.click()
