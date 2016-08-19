#-*_coding:utf8-*-
import requests
from bs4 import BeautifulSoup
import time


def get_link(packagename):
    l_cn = '&hl=zh_CN'
    l_en = '&hl=en'
    link = 'https://play.google.com/store/apps/details?id=' + '' + packagename.strip('\n') + l_en
    # link = 'https://dafasdfadsgfads.gegegeg.com'
    return link

def get_soup(link):
    link = link.strip('\n')
    soup = None
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def get_category(soup):
    category = 'NULL_CATEGORY'
    if soup is not None:
        tag_a = soup.find('a', attrs={'class': 'document-subtitle category'})
        if tag_a is not None:
            if tag_a.span is not None:
                category = tag_a.span.string

    return category

def get_name(soup):
    name = 'NULL_NAME'
    if soup is not None:
        tag = soup.find('div', attrs={'class': 'id-app-title'})
        if tag is not None:
            s = tag.string
            if s is not None:
                name = s
    return name

def get_price(soup):
    price = 'NULL_PRICE'

    if soup is not None:
        tag = soup.find('button', attrs={'class': 'price buy id-track-click id-track-impression'})
        if tag is not None:
            tag_price = tag.find('meta', attrs={'itemprop': 'price'})
            if tag_price is not None:
                s = tag_price['content']
                if s is not None:
                    price = s
    return price


def get_size(tag):

    size = 'NULL_SIZE'
    if tag is not None:
        tag_size = tag.find('div', attrs={'itemprop': 'fileSize'})
        if tag_size is not None:
            s = tag_size.string
            if s is not None:
                size = s
    return size

def get_installs(tag):
    installs = 'NULL_INSTALLS'
    if tag is not None:
        tag_download = tag.find('div', attrs={'itemprop': 'numDownloads'})
        if tag_download is not None:
            s = tag_download.string
            if s is not None:
                installs = s
    return installs

def get_sys(tag):
    android = 'NULL_ANDROID'
    if tag is not None:
        tag_sys = tag.find('div', attrs={'itemprop': 'operatingSystems'})
        if tag_sys is not None:
            s = tag_sys.string
            if s is not None:
                android = s
    return android


def get_detail_tag(soup):

    tag_detial_content = None
    if soup is not None:
        tag_detial_content = soup.find('div', attrs={'class': 'details-section metadata'})

    return tag_detial_content

def test():
    package = 'com.google.android.apps.giant'
    print(get_link(package))

    soup = None

    link = get_link(package)
    try:
        soup = get_soup(link)
    except:
        print('catch error')

    # get category
    print('-- category', get_category(soup))

    details = get_detail_tag(soup)

    # get size
    print('-- size', get_size(details))

    # get name
    print('-- name', get_name(soup))

    # get installs
    print('-- installs', get_installs(details))

    # get Android version
    print('-- android', get_sys(details))

    print('-- price', get_price(soup))

    return

test()