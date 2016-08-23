#-*_coding:utf8-*-
import file_utils as fu
import os
import get_info_from_gp as ai
import db.db_appinfo as afh
import pprint

CSV_SEP = '#'
RETURN_STR = '\n'
IN_FNAME = 'mj_package_list.txt'

def do():
    fname = IN_FNAME
    db_helper = afh.AppInfoHelper()
    path = os.path.join(fu._get_in_dir_path(), fname)
    f = open(path, encoding='utf-8')
    i = 1
    while 1:
        print('#', i)
        package = f.readline()
        package = afh.trim_package(package)
        if not package:
            break

        # get the app info from the google play
        info = ai.get_app_info(package)
        print(info)

        # save to db
        db_helper.and_or_update_by(info)

        i = i + 1
    f.close()

do()