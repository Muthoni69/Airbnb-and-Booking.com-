from bs4 import BeautifulSoup
from urllib import request
import requests
from time import sleep
from random import randint
from csv import writer

url = "https://www.airbnb.com/s/United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=2&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&checkin=2022-12-23&checkout=2022-12-27&price_min=10&price_max=1000&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&query=United%20States"

with open('Bookings US(23-27).csv', 'w', encoding='utf8', newline='') as file:
    thewriter = writer(file)

    header = ['Title', 'Beds', 'Location', 'Price', 'Reviews', 'Host']
    thewriter.writerow(header)

    
    def scrape_page(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')
        get_data(soup)

        next_page_link = soup.find('a', class_='_1bfat5l')
        if next_page_link is not None:
            href = next_page_link.get("href")
            next_url = 'https://www.airbnb.com' + f'{href}'
            scrape_page(next_url)
        else:
            print('Done')
    def get_data(soup):
        for listing in soup.select('[itemprop=itemListElement]'):
            name = listing.find("meta", itemprop="name")
            beds = listing.find('span', class_="dir dir-ltr")
            location = listing.find('div', class_="t1jojoys")
            price = listing.find('span', class_='a8jt5op').text
            reviews = listing.find('span', class_="r1dxllyb")
            host = listing.find('div', class_="t1mwk1n0")
            

            info = [name, beds, location, price, reviews, host]
            thewriter.writerow(info)
        x = randint(1,10)
        sleep(x)
        print(f'I waited for {x} seconds')
    def main():
        scrape_page(url)
        
    if __name__ == "__main__":
        main()
        
        
    



