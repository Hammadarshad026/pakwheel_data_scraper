import requests
from bs4 import BeautifulSoup
import json
import csv
import time
import os 
headers = ["Model Name", "Manufacturer", "Registered In", "Model Date", "Fuel Type", "Transmission", "Color", "Body Type", "Engine Displacement", "Driven", "Price", "page_link"]


if not os.path.exists('vichle_data.csv'):
    # Open the CSV for writing
    with open("vichle_data.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # write column headers

def file_saver(model_name="", manufacturer="", key="", model_date="", fuel_type="",transmission="", color="", body_type="", engine_displacement="", Milage="", price="", link=""):
    #save in the file 
    with open("vichle_data.csv", mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([model_name, manufacturer, key, model_date, fuel_type,transmission, color, body_type, engine_displacement, Milage, price, link]) 

def scraper(key,value,):
    print(value)
    
    url=value[0]
    Flag=True
    page_counter=0
    while Flag==True and page_counter<value[1]:
        header={
            'User-Agent':'Mozilla/5.0'
        }
        re=requests.get(url,headers=header)
        Soup=BeautifulSoup(re.content,'html.parser')
        cars_profile_links=Soup.find_all('a',class_="car-name")
        # print(cars_profile_links)
        # print(len(cars_profile_links))
        if cars_profile_links:
            for car in cars_profile_links:
                car_profile_href=car.get('href')

                car_profile_link='https://www.pakwheels.com'+car_profile_href   #carprofile link
                print(car_profile_link)

                car_profile_re=requests.get(car_profile_link,headers=header)
                Soup_car_profile=BeautifulSoup(car_profile_re.content,'html.parser')
                car_name_div=Soup_car_profile.find('div',class_='well')
                if car_name_div:                                                   #car model name
                    car_name_tag=car_name_div.find('h1')                      
                    car_name=car_name_tag.text.strip()
                    print(f"Name:  {car_name}")

                year_tag = Soup_car_profile.select_one('span.year ~ p a') #car model year
                if year_tag:
                    car_model_year = year_tag.get_text(strip=True)
                    print(f'Car_model: {car_model_year}')

                millage_tag = Soup_car_profile.select_one('span.millage ~ p')      #car millage
                if millage_tag:
                    car_millage = millage_tag.get_text(strip=True)
                    # print(f'millage: {car_millage}')
                
                fuel_type_tag = Soup_car_profile.select_one('span.type ~ p')      #fuel_type
                if fuel_type_tag:
                    car_fuel_type = fuel_type_tag.get_text(strip=True)
                    # print(f'fuel_type: {car_fuel_type}')
                
                transmission_tag = Soup_car_profile.select_one('span.transmission ~ p')      #transmission
                if transmission_tag:
                    car_transmission = transmission_tag.get_text(strip=True)
                    # print(f'transmission: {car_transmission}')

                
                
            
                color = None
                engine_capacity = None
                body_type = None

                
                ul_tag = Soup_car_profile.find('ul', id='scroll_car_detail')
                if ul_tag:
                    li_tags = ul_tag.find_all('li')
                    i = 0
                    while i < len(li_tags):
                        label = li_tags[i].get_text(strip=True)
                        if label == "Color":
                            color = li_tags[i + 1].get_text(strip=True)
                        elif label == "Engine Capacity":
                            engine_capacity = li_tags[i + 1].get_text(strip=True)
                        elif label == "Body Type":
                            body_type = li_tags[i + 1].get_text(strip=True)
                        i += 1
                    
                    # print("Color:" ,color)
                    # print("Engine",engine_capacity)
                    # print("Body capacity",body_type)

                    script_tag = Soup_car_profile.find_all("script", type="application/ld+json")
                    if script_tag:
                        car_data=None
                        for script in script_tag:
                            if script.string:
                                try:
                                    if json.loads(script.string):
                                        json_data = json.loads(script.string)
                                        if isinstance(json_data, dict) and (
                                            json_data.get('@type') == 'Product' or
                                            (isinstance(json_data.get('@type'), list) and 'Product' in json_data.get('@type'))
                                        ):
                                            car_data = json_data
                                            break
                                except Exception as e:
                                    continue
                    if car_data:
                        if car_data.get("manufacturer"):
                            manufacturer = car_data.get("manufacturer")
                        if car_data.get("offers", {}).get("price"):
                            price = car_data.get("offers", {}).get("price")
                        # print("Manufacturer:", manufacturer)
                        # print("Price:", price) 
                        # print("Registered In:",key)

                        
                                            
                file_saver(car_name, manufacturer, key, car_model_year,car_fuel_type,car_transmission, color, body_type, engine_capacity, car_millage, price, car_profile_link)
                print("________________________________________________________")
                                            
                                
                                    
                                
        print("1stUrl: ",url)                         
        page_counter +=1
        print(f"page has been completed: {page_counter}")
        print(f"moving to next page..................................")

        
        if Soup.find('li',class_="next_page").find('a'):
           next_link_tag = Soup.find('li',class_="next_page").find('a')
           nextpagelink=next_link_tag['href']

        #next page link scrape and work
        if nextpagelink:
            
            url="https://www.pakwheels.com"+nextpagelink
            print("URL: ",url)
            print("next_page_url: ",url)
        else:
            print(f"Tottal extracted pages: {page_counter}")
            print('The pages was ended')
            Flag=False

        





links={
'punjab':['https://www.pakwheels.com/used-cars/punjab/201902',1000],
 'sindh':['https://www.pakwheels.com/used-cars/sindh/201932',1000],
 'KPK':['https://www.pakwheels.com/used-cars/kpk/201917',1000],
 'balochistan':['https://www.pakwheels.com/used-cars/balochistan/201947',1000],
 'azad-kashmir':['https://www.pakwheels.com/used-cars/azad-kashmir/201953',1000]

}
# 'punjab':'https://www.pakwheels.com/used-cars/punjab/201902',
for i , (key,value) in enumerate(links.items()):

    scraper(key,value)

print("All data has been scraped..............")