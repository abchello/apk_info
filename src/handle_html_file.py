#-*_coding:utf8-*-
import inspect
import os
import shutil
from bs4 import BeautifulSoup
import file_utils as fu

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


def get_chart_info_tag(soup):
    tag = None
    if soup is not None:
        tag_h3 = soup.find('h3', attrs={'class': 'dashboard-sub-header'})
        if tag_h3 is not None:
            tag = tag_h3
    return tag


def get_chart_info_country(tag_h3):

    country = 'UNKNOWN_COUNTRY'
    # print(tag_h3)

    if tag_h3 is not None:
        s = tag_h3.contents[0]
        if s is not None and s != '':
            country = s
    return country

def get_chart_info_date(tag):

    date = 'UNKNOWN_DATE'

    if tag is not None:
        span = tag.span
        if span is not None:
            sub_span = span.span
            if sub_span is not None:
                s = sub_span.string
                if s is not None and s != '':
                    date = s
    return date




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

APP_NAME_STR = 'name'
APP_PACKAGE_STR = 'package'
APP_PUBLISHER_STR = 'publisher'

CHART_INFO_COUNTRY = 'COUNTRY'
CHART_INFO_DATE = 'DATE'

def dict_to_str(dict):
    sep = '##'
    str = '' + dict[APP_NAME_STR] + sep + dict[APP_PACKAGE_STR] + sep + dict[APP_PUBLISHER_STR]
    return str

def explain_html(path):
    soup = BeautifulSoup(open(path, encoding='utf-8'), 'html.parser')
    # print(soup.prettify(encoding='utf-8'))
    # find TAG = td

    tag = get_chart_info_tag(soup);
    country = get_chart_info_country(tag)
    date = get_chart_info_date(tag)
    print(country)
    print(date)

    fu.get_print_file_path((country.join(date)))

    dictlist_1 = []
    dictlist_2 = []
    dictlist_3 = []
    dictlist_4 = []  # [dict, dict, dict]
    dictlist_5 = []  # [dict, dict, dict]
    write_to_file_list = []  # [list, list, list]
    count = 0
    for tag_td in soup.find_all('td'):
        print('find a tag = td')
        # find the main info div tag
        tag_td_div_main_info = tag_td.find('div', attrs={'class': 'main-info'})
        # print('find a div main info :', tag_td_div_main_info)

        app_name = get_app_name_from_div_tag(tag_td_div_main_info)

        app_package = get_app_package_from_div_tag(tag_td_div_main_info)

        app_publisher = get_app_publisher_from_div_tag(tag_td_div_main_info)

        app_info_dict = {APP_NAME_STR: app_name, APP_PACKAGE_STR: app_package, APP_PUBLISHER_STR: app_publisher}

        column = count % 5
        if column == 0:
            dictlist_1.append(app_info_dict)
        elif column == 1:
            dictlist_2.append(app_info_dict)
        elif column == 2:
            dictlist_3.append(app_info_dict)
        elif column == 3:
            dictlist_4.append(app_info_dict)
        elif column == 4:
            dictlist_5.append(app_info_dict)

        print('count :', count)
        print('column :', column + 1)

        count += 1
        sep = '##'
        # print('----#' + str(count) + sep + app_name + sep + app_package + sep + app_publisher)
        print('---#' + str(count) + str(app_info_dict))

    # init the list of write to file
    write_to_file_list.append(dictlist_1)
    write_to_file_list.append(dictlist_2)
    write_to_file_list.append(dictlist_3)
    write_to_file_list.append(dictlist_4)
    write_to_file_list.append(dictlist_5)

    for i in range(len(write_to_file_list)):
        # write the dict to file
        list = write_to_file_list[i]
        for s_dict in list:
            # line = dict_to_str(s_dict)
            line = s_dict[APP_PACKAGE_STR]
            print('write-->line:', line)
            path = fu.get_out_file_path(str(i))
            fu.write_text(path, line)


    print('------- END --------')
    print('dictlist_1 length is :', len(dictlist_1))
    print('dictlist_5 length is :', len(dictlist_5))

    # print(soup.td)

    # print(soup.td.contents)
# fu.clean()
# fu.create_out_dir()
explain_html(get_file_path())