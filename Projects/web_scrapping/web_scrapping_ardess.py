from datetime import datetime
from bs4 import BeautifulSoup
import requests
from csv import writer


def find_laptop():
    # searched_model = input(f'Please enter the desire model:').lower()
    searched_model = 'legion'
    # Bypass Proxy
    proxies = {"http": None, "https": None}
    html_text = requests.get('https://ardes.bg/laptopi/laptopi/lenovo/pamet-kapatsitet-pamet-ot-32-do-32/za-igri', proxies=proxies).text
    soup = BeautifulSoup(html_text, 'lxml')
    laptops = soup.find_all('div', class_='product')
    today = datetime.now()
    curr_time = f'{today.date()}_{today.hour}_{today.minute}'
    with open(f'C:\\Users\\alexander.kirilov\\Desktop\\Laptop\\Result_from_ARDESS_{curr_time}.csv', 'w', newline='', encoding='cp1251') as f:
        the_writer = writer(f)
        header = ['Model', 'Parameters', 'Price']
        the_writer.writerow(header)

        for index, laptop in enumerate(laptops):
            laptop_name = laptop.find('div', class_="isTruncated").text.replace('Лаптоп', '')
            if searched_model in laptop_name.lower():
                laptop_parameters = laptop.find('ul', class_="parameters list-unstyled parameters-ellipsis").text
                laptop_price = laptop.find('span', class_='price-num').text
                laptop_price_sub = laptop.find('sup', class_='price-sup').text
                laptop_accurate_price = laptop_price.replace(laptop_price_sub, '')
                info = [laptop_name, laptop_parameters, laptop_accurate_price]
                the_writer.writerow(info)

find_laptop()

# For looping the program every 24 hours
''''if __name__ == '__main__':
    while True:
        find_laptop()
        wait_time = 86400
        print(f'The File was created, wait more {wait_time} seconds or {round(wait_time/3600)} hours for the next file')
        time.sleep(86400)'''''