#-*_coding:utf8-*-
import file_utils as fu
import os
import get_info_from_gp as ai
import db.db_appinfo as afh

CSV_SEP = '#'
RETURN_STR = '\n'
IN_FNAME = 'mj_package_list.txt'

def do():
    fname = IN_FNAME
    path = os.path.join(fu._get_in_dir_path(), fname)
    f = open(path, encoding='utf-8')
    i = 1
    while 1:
        print('#', i)
        package = f.readline()
        if not package:
            break

        # get the app info from the google paly
        info = ai.get_app_info(package)
        print(info)

        # save to db
        db_helper = afh.AppInfoHelper()
        db_helper.and_or_update_by(info)

        i = i + 1
    f.close()


def do_test():

    appinfohelper = afh.AppInfoHelper()
    appinfohelper.add_or_update('com.kingsoft.bb', 'hello version4', 'Business', '21M', 'HK23.9', '100000', 'Nicholas')

do()