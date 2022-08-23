from datetime import datetime
from bs4 import BeautifulSoup
import requests
from csv import writer


def find_laptop():
    # searched_model = input(f'Please enter the desire model:').lower()
    searched_model = 'Legion'
    # Bypass Proxy
    proxies = {"http": None, "https": None}
    html_text = requests.get("https://www.jarcomputers.com/Lenovo/Laptopi_cat_2.html?ref=catundefined&fprop[1103][5688]=5688&order=-1", proxies=proxies).text
    soup = BeautifulSoup(html_text, 'lxml')
    today = datetime.now()
    curr_time = f'{today.date()}_{today.hour}_{today.minute}'
    with open(f'C:\\Users\\alexander.kirilov\\Desktop\\Laptop\\Result_from_JARCOMPUTERS_{curr_time}.csv', 'w', newline='', encoding='cp1251') as f:
        the_writer = writer(f)
        header = ['Model', 'Parameters', 'Price']
        the_writer.writerow(header)

        result = soup.find('ol', id='product_list')
        laptops = result.find_all('div', class_='s2')
        for laptop in laptops:
            laptop_name = laptop.find('a', class_='plttl').text.split(', ')[0].replace(',', '\n')
            if searched_model.lower() in laptop_name.lower():
                laptop_descr = laptop.find('a', class_='plttl').text.split(', ')[1:]
                laptop_price = laptop.find('div', class_='price').text
                laptop_descr_final = '\n'.join([el for el in laptop_descr])
                info = [laptop_name, laptop_descr_final, laptop_price]
                the_writer.writerow(info)

find_laptop()
