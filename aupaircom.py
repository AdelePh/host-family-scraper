# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:48:35 2022

@author: minhp
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd

count = 0
next_page = True
all_family = []
while next_page == True:
    family_each_page = []
    url = 'https://www.aupair.com/find_family.php?quick_search=search&language=fr&page='+str(count)
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), 'html.parser')
    content = bs.find('div',{'class':'middleContentBox leftMenuMiddleContentBox'})
    for family in content.findAll('a', href = re.compile('^(/fr/emploi-aupair)')):
        if 'href' in family.attrs:
            family_each_page.append('https://www.aupair.com'+ family.attrs['href'])
            print('https://www.aupair.com'+ family.attrs['href'])
    if len(family_each_page) != 0:        
        all_family.append(family_each_page)
        count = count + 1
    else:
        next_page = False
    
flat_list = [item for sublist in all_family for item in sublist]

df = pd.DataFrame({'families':flat_list})

df.to_excel('link_to_all_families.xlsx')