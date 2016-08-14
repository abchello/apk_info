import requests
from bs4 import BeautifulSoup

url_str = 'https://play.google.com/store/apps/details?id=com.facebook.moments'
url_str_1 = 'https://play.google.com/store/apps/details?id=tw.mobileapp.qrcode.banner'
url_str_2 = 'https://play.google.com/store/apps/details?id=com.iscreenrecorder&hl=zh_CN'
response = requests.get(url_str_2)
# soup = BeautifulSoup(response.text)
# soup = BeautifulSoup(response.text,'lxml')
soup = BeautifulSoup(response.text, "html.parser")
tag_str = 'span'
# span = soup.find('span')
# print(span)
# for x in soup.find_all('span'):
#     print(x.text)

for x in soup.find_all("span", {"itemprop": "genre"}):
    print(x.text)
