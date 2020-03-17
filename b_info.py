#!/usr/bin/python3

# Author: Mohammad Shiblee Noman Ahad
# Email: hello@iamahad.com
# Website: www.iamahad.com
# Github: www.github.com/i-am-ahad


"""Bikroy Info module for for fetching users data from indivisual links"""


import  requests
import bs4

def getInformation(url):
    res = requests.get(url)
    res.raise_for_status()
    soup  = bs4.BeautifulSoup(res.text,'html.parser')

    phone_selector = soup.select('#phones > div > ul > li > span')
    name_selector = soup.select('body > div.app-content > div > div.ui-panel.is-rounded.item-detail > div > div:nth-child(1) > div.item-top.col-12.lg-8 > p > span.poster')
    location_selector = soup.select('body > div.app-content > div > div.ui-panel.is-rounded.item-detail > div > div:nth-child(1) > div.item-top.col-12.lg-8 > p > span.location')
    try:
        phone = phone_selector[0].text.strip()
        name = name_selector[0].text.strip()
        name = name[12:]
        location = location_selector[0].text.strip()
    except:
        print('Information Not Given\n')
        
    try:
        print('------BIKROY.COM USER------')
        print(name)
        print(phone)
        print(location)
        print()
    except:
        print('No Info\n')
        
    return 