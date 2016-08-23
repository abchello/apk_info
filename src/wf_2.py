#-*_coding:utf8-*-
import db.db_appinfo as afh
import constants as cons
import leancloud

class AppInfo(leancloud.Object):
    pass

def do():
    db_helper = afh.AppInfoHelper()

    list = db_helper.query()
    return
    print(list)
    for inf in list:
        print(inf.id)
        print(inf[cons.FIELD_PACKAGE])

    print(list.count())

do()