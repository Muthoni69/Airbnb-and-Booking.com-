from bs4 import BeautifulSoup
import requests
from csv import writer
from time import sleep
from random import randint


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

url = "https://www.booking.com/searchresults.en-gb.html?ss=United+Kingdom&sb_entire_place=1&ssne=United+Kingdom&ssne_untouched=United+Kingdom&efdco=1&label=gog235jc-1DCAEoggI46AdIM1gDaHaIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4Aoen1ZkGwAIB0gIkMDA3ZGM4OGMtNWU5Zi00OWY4LWE2MzMtZjM2M2JiOWUzMDE12AIE4AIB&sid=dab61b77e2903bba6d356b91f89786a9&aid=397594&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=222&dest_type=country&checkin=2022-12-23&checkout=2022-12-27&group_adults=2&no_rooms=2&group_children=0&sb_travel_purpose=leisure&nflt=privacy_type%3D3%3Bprivacy_type_no_date%3D3"
with open('Listings UK(23-27).csv', 'w', encoding='utf8', newline='') as file:
    thewriter = writer(file)

    header = ['Name', 'Roomsinfo', 'Beds', 'Location', 'DiscountPrice', 'ActualPrice', 'Reviews', 'Host']
    thewriter.writerow(header)

    def scrape_page(url):
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')
        get_data(soup)
    
        for page in range(25, 925, 25):
            next_url = "https://www.booking.com/searchresults.en-gb.html?ss=United+Kingdom&sb_entire_place=1&ssne=United+Kingdom&ssne_untouched=United+Kingdom&efdco=1&label=gog235jc-1DCAEoggI46AdIM1gDaHaIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4Aoen1ZkGwAIB0gIkMDA3ZGM4OGMtNWU5Zi00OWY4LWE2MzMtZjM2M2JiOWUzMDE12AIE4AIB&sid=dab61b77e2903bba6d356b91f89786a9&aid=397594&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=222&dest_type=country&checkin=2022-12-23&checkout=2022-12-27&group_adults=2&no_rooms=2&group_children=0&sb_travel_purpose=leisure&nflt=privacy_type%3D3%3Bprivacy_type_no_date%3D3 &offset={page}".format(page= page)
            
            page = requests.get(next_url, headers=headers)
            soup = BeautifulSoup(page.content, 'lxml')
            get_data(soup)
            #scrape_page(next_url)
    
    def get_data(soup):
        for list in soup.select('[data-testid=property-card]'):
            name = list.find('div', class_='fcab3ed991').text
            roomsinfo = list.find('div', class_='cb5b4b68a4').text
            beds = list.find('span', class_='bb58e7a787')
            location = list.find('span', class_="f4bd0794db b4273d69aa").text
            discountprice = list.find('span', class_="fcab3ed991 bd73d13072")
            actualprice = list.find('span', class_="a0c113411d e293a04099")
            reviews = list.find('div', class_="b5cd09854e d10a6220b4")
            host = list.find('div', class_="b5cd09854e f0d4d6a2f5 e46e88563a")

            info = [name, roomsinfo, beds, location, discountprice, actualprice, reviews, host]
            thewriter.writerow(info)
            
            #print(location)
        x = randint(1,10)
        sleep(x)
        print(f'I waited for {x} seconds')
    def main():
        scrape_page(url)
        
    if __name__ == "__main__":
        main()
        

        
    


