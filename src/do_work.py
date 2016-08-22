#-*_coding:utf8-*-
import file_utils as fu
import os
import get_info_from_gp as ai
import db.db_appinfo as afh

CSV_SEP = '#'
RETURN_STR = '\n'
IN_FNAME = 'mj_package_list.txt'
OUT_FNAME_TAG = 'app_info_2108'

def get_package_list():
    fname = IN_FNAME
    path = os.path.join(fu._get_in_dir_path(), fname)
    f = open(path, encoding='utf-8')
    i = 1
    while 1:
        print('#', i)
        package = f.readline()
        if not package:
            break
        info = output_line_by(package).strip(RETURN_STR)
        print(info)
        path_out = fu.get_out_file_path(OUT_FNAME_TAG)
        fu.write_text(path_out, info)
        i = i + 1
    f.close()

def delete_whitespace_from_start_end(s):
    str = ''
    if s is not None:
        str = s.lstrip().rstrip()
    return str

def output_line_by(package):

    print(ai.get_link(package))

    soup = None

    link = ai.get_link(package)
    try:
        soup = ai.get_soup(link)
    except:
        print('catch error')

    # get category
    cagegory = delete_whitespace_from_start_end(ai.get_category(soup))
    print('-- category', cagegory)

    details = ai.get_detail_tag(soup)

    # get size
    size = delete_whitespace_from_start_end(ai.get_size(details))
    print('-- size', size)

    # get name
    name = ai.get_name(soup)
    print('-- name', name)

    # get installs
    installs = delete_whitespace_from_start_end(ai.get_installs(details))
    print('-- installs', installs)

    # get Android version
    androidv = delete_whitespace_from_start_end(ai.get_sys(details))
    print('-- android', androidv)

    # get price
    price = delete_whitespace_from_start_end(ai.get_price(soup))
    print('-- price', price)

    out_str = package.strip(RETURN_STR) + CSV_SEP + name + CSV_SEP + cagegory + CSV_SEP + price + CSV_SEP + installs + CSV_SEP + androidv + RETURN_STR

    return out_str

def do_test():

    appinfohelper = afh.AppInfoHelper()
    appinfohelper.add_or_update('com.kingsoft.bb', 'hello version4', 'Business', '21M', 'HK23.9', '100000', 'Nicholas')

do_test()