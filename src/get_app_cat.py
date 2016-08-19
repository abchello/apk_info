#-*_coding:utf8-*-
import requests
from bs4 import BeautifulSoup


def get_link_path(packagename):
    path = 'https://play.google.com/store/apps/details?id='+ '' + packagename.strip('\n') + '&hl=zh_CN'
    return (path)

def get_catalog(link):
    link=link.strip('\n')
    response = requests.get(link)
    # print('get link:' + link)
    soup = BeautifulSoup(response.text, "html.parser")
    catalog_str = ''

    for x in soup.find_all("span", {"itemprop": "genre"}):
        catalog_str = x.text
    #     # print(catalog_str)

    return catalog_str

def get_app_name(link):
    link=link.strip('\n')
    response = requests.get(link)
    # print('get link:' + link)
    soup = BeautifulSoup(response.text, "html.parser")
     # get the app name
    app_name_str = ''
    for x in soup.find_all("div", {"class": "id-app-title"}):
        app_name_str = x.text
    return app_name_str

def write_text(text):
    output_path = 'D:/Personal/Google Drive/Workspce/2016_Q1/Meizu/Coding/html/file/package_1_output.txt'
    f = open(output_path,'a',encoding='utf-8')
    f.write(text)
    f.write('\n')
    f.close()

# D:\Personal\Google Drive\Workspce\2016_Q1\Meizu\Coding\html\file
f = open('D:/Personal/Google Drive/Workspce/2016_Q1/Meizu/Coding/html/file/package_1.txt', encoding='utf-8')
i = 1;
while 1:
    print( '#', i )
    packagename = f.readline()
    if not packagename:
        break
    url = get_link_path(packagename);
    url = url.strip('\n')
    print(url)
    info = packagename.strip('\n') + ',' + get_app_name(url) + ',' + get_catalog(url)
    print(info)
    write_text(info)
    i = i+1
f.close()