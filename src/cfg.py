import json
import os, inspect

CFG_F_NAME = 'key.json'
KEY_APPID = 'AppID'
KEY_APPKEY = 'AppKey'
KEY_MASTERKEY = 'MasterKey'


def read_key():

    # file_path = os.path.join(os.getcwd(), CFG_F_NAME)
    # the os.getcwd return the path of the scrip of the execute
    dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    print('dir is -->', dir)
    file_path = os.path.join(dir, CFG_F_NAME)
    print(file_path)
    with open(file_path) as data_file:
        key = json.load(data_file)
        mkey = key[KEY_MASTERKEY]
        print(mkey)
    return key


def get_app_key():
    return read_key()[KEY_APPKEY]


def get_app_id():
    return read_key()[KEY_APPID]


def get_master_key():
    return read_key()[KEY_MASTERKEY]


def write_cfg_file():
    cfg_fname = os.path.join(os.getcwd(), CFG_F_NAME)
    if os.path.isfile(cfg_fname):
        return
    cfg = {KEY_APPID: '', KEY_APPKEY: '', KEY_MASTERKEY: ''}
    with open(cfg_fname, 'w') as f:
        json.dump(cfg, f)


