#-*_coding:utf8-*-
import db.dbhelper as afh
import constants as cons

def do():
    db_helper = afh.AppInfoHelper()

    list = db_helper.query()
    print(list)
    i = 0
    for inf in list:
        print('#', i)
        package = inf.get(cons.FIELD_PACKAGE)
        new_pkg = afh.trim_package(package)
        inf.set(cons.FIELD_PACKAGE, new_pkg)
        inf.save()
        i += 1

    # print(list.count())

do()
