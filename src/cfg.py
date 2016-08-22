import json
import os
from pprint import pprint


CFG_F_NAME = 'key.json'
KEY_APPID = 'AppID'
KEY_APPKEY = 'AppKey'
KEY_MASTERKEY = 'MasterKey'

key_set = None

def read_key():

    file_path = os.path.join(os.getcwd(), CFG_F_NAME)
    print(file_path)
    with open(CFG_F_NAME) as data_file:
        key = json.load(data_file)
        id = key[KEY_APPID]
        appkey = key[KEY_APPKEY]
        mkey = key[KEY_MASTERKEY]
        # pprint(key)
        print(mkey)
        key_set = key
    return key

def get_app_key():
    if key_set is None:
        read_key()
    return read_key()[KEY_APPKEY]

def get_app_id():
    if key_set is None:
        read_key()
    return read_key()[KEY_APPID]

def get_master_key():
    if key_set is None:
        read_key()
    return key_set[KEY_MASTERKEY]

def write_cfg_file():
    cfg_fname = os.path.join(os.getcwd(), CFG_F_NAME)
    if os.path.isfile(cfg_fname):
        return
    cfg = {KEY_APPID: '', KEY_APPKEY: '', KEY_MASTERKEY: ''}
    with open(cfg_fname, 'w') as f:
        json.dump(cfg, f)


