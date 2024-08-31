from driver import Driver
from bs4 import BeautifulSoup
import requests


response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "html.parser")

data = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")

link_list = [anchor.get("href") for anchor in data]
address_list = [' '.join(anchor.text.split()) for anchor in data]
price_list = [price.text[:6] for price in prices]

last_data = {}

for i in range(1, len(link_list) + 1):
    last_data[i] = [address_list[i - 1], price_list[i - 1], link_list[i - 1]]

print(last_data)
for (key, data) in last_data.items():
    driver = Driver()
    driver.send_data(data[0], data[1], data[2])
