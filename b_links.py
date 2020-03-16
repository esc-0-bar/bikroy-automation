# Author: Mohammad Shiblee Noman Ahad
# Email: hello@iamahad.com
# Website: www.iamahad.com
# Github: www.github.com/i-am-ahad


"""Bikroy Links module for for getting links from main page everytime it refreshes"""


import bs4
import  requests

links = []

def getPageLinks(mainPageUrl):
    res = requests.get(mainPageUrl)
    res.raise_for_status()
    soup  = bs4.BeautifulSoup(res.text,'html.parser')

    for ads in range(1,28):
        try:        
            selector = str(soup.select('#app-wrapper > div > div:nth-child(3) > div > div > div.row--3Vhjr.main-container--28aG5.justify-content-flex-start--1Xozy.align-items-normal--vaTgD.flex-wrap-wrap--2PCx8.flex-direction-row--27fh1.flex--3fKk1 > div.sm-col-12--30zDS.lg-col-9--20qCf.block--3v-Ow > div > div > div:nth-child(2) > div.ad-list--2Y3ql > div.list-wrapper--t_A02 > ul > li:nth-child(%d) > a'%ads))
            selector_parts =selector[29:200].split('"')
            link = 'https://bikroy.com/'+selector_parts[1]
            selector_parts.clear()
            links.append(link)
        except:
            print("Nothing Found %d"%ads)
    return links