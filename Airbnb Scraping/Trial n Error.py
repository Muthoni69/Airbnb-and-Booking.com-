
from pkgutil import get_data
from urllib import request, response
from bs4 import BeautifulSoup, SoupStrainer
import requests
from csv import writer
from requests_html import HTMLSession
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from time import sleep
from random import randint

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

session = HTMLSession()
url = "https://www.airbnb.com/s/United-Kingdom/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&place_id=ChIJqZHHQhE7WgIReiWIMkOg-MQ&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')


lists = soup.select('[itemprop=itemListElement]')
    
for listing in lists:
    name = listing.find("meta", itemprop="name")
    beds = listing.find('span', class_="dir dir-ltr")
    location = listing.find('div', class_="t1jojoys")
    price = listing.find('span', class_='a8jt5op')
    reviews = listing.find('span', class_="r1dxllyb")
    host = listing.find('div', class_="t1mwk1n0")

    print(beds)
        
    
        
x = randint(1,10)
sleep(x)
print(f'I waited for {x} seconds')
#print(location)
    


    
    




