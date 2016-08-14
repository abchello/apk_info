#-*_coding:utf8-*-

import os
import shutil

def _get_in_dir_path():

    curr_path = os.getcwd()
    print('current path:' + curr_path)

    # the 'in' directory path
    in_dir_path = curr_path + '/in'

    return in_dir_path

def _get_out_dir_path():

    curr_path = os.getcwd()

    # the 'out' directory path
    out_dir_path = curr_path + '/out'

    return out_dir_path


def create_ou_dir():

    in_dir_path = _get_in_dir_path()

    # make the 'in' dir
    if not os.path.exists(in_dir_path):
        os.makedirs(in_dir_path)
        print('Create "in" folder success')
    else:
        print('"in" folder exist')

    return

def create_out_dir():

    out_dir_path = _get_out_dir_path()

    # make the 'out' dir
    if not os.path.exists(out_dir_path):
        os.makedirs(out_dir_path)
        print('Create "out" folder success')
    else:
        print('"out" folder exist')

    return

def clean():
    if os.path.exists(_get_in_dir_path()):
        shutil.rmtree(_get_in_dir_path())
    if os.path.exists(_get_out_dir_path()):
        shutil.rmtree(_get_out_dir_path())

clean()
create_ou_dir()
create_out_dir()