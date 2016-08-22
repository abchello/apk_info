import leancloud
import cfg
import pprint

FORM_NAME = 'AppInfo'
FIELD_PACKAGE = 'package'
FIELD_NAME = 'name'
FIELD_CATEGORY = 'category'
FIELD_SIZE = 'size'
FIELD_INSTALLS = 'installs'
#FIELD_PROVIDER = 'provider'
FIELD_PRICE = 'price'
FIELD_OFFERED = 'offered'


class DBBase(object):

    form_name = ''

    def initialize_sdk(self):
        leancloud.init(cfg.get_app_id(), cfg.get_app_key())
        print('DBBase init() -- called')

class AppInfoHelper(DBBase):

    # super.form_name = FORM_NAME

    AppInfo = leancloud.Object()

    def __init__(self):
        AppInfo = leancloud.Object.extend(FORM_NAME)
        print('AppInfoHelper init() --called')

    def add_or_update(self, package, name, category, size, price, installs, offered):
        query = self.AppInfo.query
        query_list = query.equal_to(FIELD_PACKAGE, package).find()
        appinfo = None
        if query_list.count() > 0:
            id = query_list[0].id
            appinfo = self.AppInfo.create_without_data(id)
        else:
            appinfo = self.AppInfo()
            appinfo.set(FIELD_PACKAGE, package)

        appinfo.set(FORM_NAME, name)
        appinfo.set(FIELD_CATEGORY, category)
        appinfo.set(FIELD_PRICE, price)
        appinfo.set(FIELD_SIZE, size)
        appinfo.set(FIELD_OFFERED, offered)
        appinfo.set(FIELD_INSTALLS, installs)
        appinfo.save()

        return appinfo
