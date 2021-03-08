from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv
import re
import pandas as pd
import requests

product_list = []
list_of_product_href = []

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument('--disable-extensions')
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options, executable_path='/home/winston/Downloads/chromedriver_linux64/chromedriver')


def amazon_scraper(search=None):
    amazon = 'https://www.amazon.in'
    search = '/s?k=mobile'
    driver.get(amazon + search)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find_all('a', href=True, attrs={"class": "a-link-normal a-text-normal" })
    for link in links:
        print(link["href"])


def flipkart_scraper(search=None):
    flipkart = 'https://www.flipkart.com'
    search = '/search?q=mobile'
    driver.get(flipkart + search)

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find_all('a', href=True, attrs={"class": "s1Q9rs"})
    for link in links:
        list_of_product_href.append(link['href'])
    print(list_of_product_href)
    counter = 1
    for i in list_of_product_href:
        time.sleep(5)
        driver.get(flipkart + i)
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        name = soup.find('span', attrs={"class": "B_NuCI"})
        name = name.text.split('(')[0]
        rating = soup.find('div', attrs={"class": "_3LWZlK"})
        print(rating.text)
        price = soup.find('div', attrs={"class": "_30jeq3 _16Jk6d"})
        print(price.text)
        specifications = soup.find('li', attrs={"class": "_21Ahn-"})
        print(specifications.text)
        model = ''
        models = soup.find_all('li', attrs={"class": "_21lJbe"}, text=True)[1:2]
        for i in models:
            model = i.text
        add_to_list(name, rating.text, price.text, specifications.text, model, 'Flipkart', flipkart + i)
        counter += 1
        if counter == 5:
            break

    driver.quit()


def add_to_list(name, rating, price, specs, model, source, link):
    product = {
        "Name": name,
        "Rating": rating,
        "Price": price.replace(',', ''),
        "Specifications": specs,
        "Model No.": model,
        "Source": source,
        "URL": link
    }
    product_list.append(product)


def generate_csv_flipkart():
    with open("out.csv", "w") as f:
        wr = csv.DictWriter(f, delimiter="\t", fieldnames=list(product_list[0].keys()))
        wr.writeheader()
        wr.writerows(product_list)


amazon_scraper()
#flipkart_scraper()
#generate_csv_flipkart()
