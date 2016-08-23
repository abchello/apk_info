#-*_coding:utf8-*-
import db.db_appinfo as afh


def do():
    db_helper = afh.AppInfoHelper()

    list = db_helper.query()
    for index in len(list):
        print(list[index])

    print(len(list))

do()