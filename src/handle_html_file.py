#-*_coding:utf8-*-
import inspect
import os
import shutil
from bs4 import BeautifulSoup

#Get test file path
def get_file_path():

    test_file_path = ''

    # the test dirs
    test_dir = os.path.join(os.getcwd(), 'test_file')

    # traverse the test dirs
    list_dirs = os.walk(test_dir)
    is_find_file = False
    for root, dirs, files in list_dirs:
        if is_find_file:
            break
        for f in files:
            if not f.startswith('.'):  # ignore the hide files
                file_path = os.path.join(root, f)  # get a full path
                print(os.path.join(root, f))
                if os.path.isfile(file_path):
                    test_file_path = file_path
                    is_find_file = True
                    break
    print('the file path :' + test_file_path)
    return test_file_path

def get_app_name_from_div_tag(div):
    # Default value
    info_app_name = 'NULL_APP_NAME'
    if div is None:
        return info_app_name

    # find 'span' name tag from the info div tag
    tag_td_div_span_app_name = div.find('span', attrs={'class': 'oneline-info title-info'})

    if tag_td_div_span_app_name is None:
        return info_app_name

    # may be without 'a' tag
    if tag_td_div_span_app_name.a is None:
        return info_app_name

    name = tag_td_div_span_app_name.a.string
    # get the info app name
    if name is not None:
        info_app_name = name

    print('find the app name      :' + info_app_name)
    return info_app_name

def get_app_publisher_from_div_tag(div):
    # default value
    info_app_publisher = 'NULL_APP_PUBLISHER'
    if div == None:
        return info_app_publisher

    # find the 'span' publisher tag from the info div tag
    tag_td_div_span_app_publisher = div.find('span', attrs={'class': 'oneline-info add-info'})
    if type(tag_td_div_span_app_publisher) == type(None):
        return info_app_publisher

    # may be without 'a' tag
    if tag_td_div_span_app_publisher.a is None:
        return info_app_publisher

    publisher = tag_td_div_span_app_publisher.a.string
    if publisher is not None:
        # get the info app publisher
        info_app_publisher = publisher

    print('find the app publisher :' + info_app_publisher)
    return info_app_publisher


def get_app_package_from_div_tag(div):
    # Default value
    info_app_package = 'NULL_APP_PACKAGE'

    if div is None:
        return info_app_package

    # find the 'span' publisher tag from the info div tag
    tag_td_div_span_app_package = div.find('span', attrs={'class': 'product-code'})
    if tag_td_div_span_app_package is None:
        return info_app_package

    # get the info app publisher
    package = tag_td_div_span_app_package.string
    if package is not None:
        info_app_package = package

    print('find the app package   :' + info_app_package)
    return info_app_package

    # for tag_div in tag_td.find_all('div'):
        # print('find a tag = div')
        # use method 'join' to delete the '[]' for the reason that using the 'find_all' method get string will get the last eletment call the str() and append the string '[]'
        # print('find a tag class is ', ''.join(tag_div['class']))
        # print(tag_div.attrs)
        # print(tag_div.find('span', attrs={'class': 'title-info-wrapper'}))
        # class_value = ''.join(tag_div['class'])
        # if class_value == 'main-info':
        #     print('find a main info')

def explain_html(path):
    soup = BeautifulSoup(open(path, encoding='utf-8'), 'html.parser')
    # print(soup.prettify(encoding='utf-8'))
    # find TAG = td
    count = 0
    for tag_td in soup.find_all('td'):
        print('find a tag = td')
        # find the main info div tag
        tag_td_div_main_info = tag_td.find('div', attrs={'class': 'main-info'})
        # print('find a div main info :', tag_td_div_main_info)

        app_name = get_app_name_from_div_tag(tag_td_div_main_info)

        app_package = get_app_package_from_div_tag(tag_td_div_main_info)

        app_publisher = get_app_publisher_from_div_tag(tag_td_div_main_info)
        count = count + 1
        sep = '##'
        print('----#' + str(count) + sep + app_name + sep + app_package + sep + app_publisher)

    # print(soup.td)

    # print(soup.td.contents)

explain_html(get_file_path())