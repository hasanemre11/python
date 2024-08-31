import requests
from bs4 import BeautifulSoup
import re

url = "https://www.billboard.com/charts/hot-100/2000-08-12/"

response = requests.get(url).text


soup = BeautifulSoup(response, "html.parser")

clas = "c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"

listing = soup.select("li h3")[:100]

for song in listing:
    print(re.sub(r'\s+', ' ', song.get_text()).strip())
