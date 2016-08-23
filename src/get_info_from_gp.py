#-*_coding:utf8-*-
import requests
from bs4 import BeautifulSoup
import constants as cons

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
    category = ''
    if soup is not None:
        tag_a = soup.find('a', attrs={'class': 'document-subtitle category'})
        if tag_a is not None:
            if tag_a.span is not None:
                category = tag_a.span.string

    return category

def get_name(soup):
    name = ''
    if soup is not None:
        tag = soup.find('div', attrs={'class': 'id-app-title'})
        if tag is not None:
            s = tag.string
            if s is not None:
                name = s
    return name

def get_price(soup):
    price = ''

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

    size = ''
    if tag is not None:
        tag_size = tag.find('div', attrs={'itemprop': 'fileSize'})
        if tag_size is not None:
            s = tag_size.string
            if s is not None:
                size = s
    return size

def get_installs(tag):
    installs = ''
    if tag is not None:
        tag_download = tag.find('div', attrs={'itemprop': 'numDownloads'})
        if tag_download is not None:
            s = tag_download.string
            if s is not None:
                installs = s
    return installs

def get_sys(tag):
    android = ''
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


def delete_whitespace_from_start_end(s):
    str = ''
    if s is not None:
        str = s.lstrip().rstrip()
    return str

def get_app_info(package):

    soup = None

    link = get_link(package)
    print(link)
    try:
        soup = get_soup(link)
    except:
        print('catch error')

    # get category
    cagegory = delete_whitespace_from_start_end(get_category(soup))
    print('-- category', cagegory)

    details = get_detail_tag(soup)

    # get size
    size = delete_whitespace_from_start_end(get_size(details))
    print('-- size', size)

    # get name
    name = get_name(soup)
    print('-- name', name)

    # get installs
    installs = delete_whitespace_from_start_end(get_installs(details))
    print('-- installs', installs)

    # get Android version
    androidv = delete_whitespace_from_start_end(get_sys(details))
    print('-- android', androidv)

    # get price
    price = delete_whitespace_from_start_end(get_price(soup))
    print('-- price', price)

    # get category
    print('-- category', get_category(soup))

    # get offered by
    offered = ''

    dict = {cons.FIELD_PACKAGE: package,
            cons.FIELD_NAME: name,
            cons.FIELD_SIZE: size,
            cons.FIELD_CATEGORY: cagegory,
            cons.FIELD_PRICE: price,
            cons.FIELD_INSTALLS: installs,
            cons.FIELD_ANDROID: androidv,
            cons.FIELD_OFFERED: offered}

    return dict
