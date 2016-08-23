import leancloud
import cfg
import constants as cons

# class AppInfo(leancloud.Object):
#     pass

class DBBase(object):

    def initialize_sdk(self):
        leancloud.init(cfg.get_app_id(), cfg.get_app_key())
        print('DBBase init() -- called')

class AppInfoHelper(DBBase):


    # AppInfo = leancloud.Object.extend(FORM_NAME)

    def __init__(self):
        super().initialize_sdk()
        self.AppInfo = leancloud.Object.extend(cons.FORM_NAME)
        print('AppInfoHelper init() --called')


    def and_or_update_by(self, dect):
        return self.add_or_update(dect[cons.FIELD_PACKAGE], dect[cons.FIELD_NAME],
                           dect[cons.FIELD_CATEGORY], dect[cons.FIELD_SIZE],
                           dect[cons.FIELD_PRICE], dect[cons.FIELD_INSTALLS],
                           dect[cons.FIELD_OFFERED], dect[cons.FIELD_ANDROID])

    def add_or_update(self, package, name, category, size, price, installs, offered, android):
        appinfo = None
        query = self.AppInfo.query
        query_list = query.equal_to(cons.FIELD_PACKAGE, package).find()
        if len(query_list) > 0:
            id = query_list[0].id
            appinfo = self.AppInfo.create_without_data(id)
            print('update ID-->', id)
        else:
            appinfo = self.AppInfo()
            appinfo.set(cons.FIELD_PACKAGE, package)
            print('add    ID-->', appinfo.id)

        if name is not None and name != '':
            appinfo.set(cons.FIELD_NAME, name)

        if category is not None and category != '':
            appinfo.set(cons.FIELD_CATEGORY, category)

        if price is not None and price != '':
            appinfo.set(cons.FIELD_PRICE, price)

        if size is not None and size != '':
            appinfo.set(cons.FIELD_SIZE, size)

        if offered is not None and offered != '':
            appinfo.set(cons.FIELD_OFFERED, offered)

        if installs is not None and installs != '':
            appinfo.set(cons.FIELD_INSTALLS, installs)

        if android is not None and android != '':
            appinfo.set(cons.FIELD_ANDROID, android)

        appinfo.save()

        return appinfo

class printer(object):

    def print_a(self):
        print('printA')

    def print_b(self, str):
        print('printB', str)

