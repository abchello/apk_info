#-*_coding:utf8-*-
import inspect
import os
import shutil
import ntpath
import time

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

def get_output_file_path(source_file_path):

    in_file_name = ntpath.basename(source_file_path)

    current_time_str = time.gmtime()

    print('current time string is :' + current_time_str)

    output_file_path = in_file_name + current_time_str

    print('Output file path is :' + output_file_path)

    return output_file_path

def get_file_list_from_in_dir():
    count = 0;
    for i in os.listdir(_get_in_dir_path()):
        count = (count + 1)
        print('# ', count, ' :' + i)

    return


def test_make_files():
    open(_get_in_dir_path() + '/test_file_1.txt', 'w+', encoding='utf-8').close()
    open(_get_in_dir_path() + '/test_file_2.txt', 'w+', encoding='utf-8').close()
    open(_get_in_dir_path() + '/test_file_3.txt', 'w+', encoding='utf-8').close()
    return


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

def test():

    print('current path:' + curr_path)
    print('pathsep :' + os.pathsep)
    print('path.sep :' + os.path.sep)
    print('os.sep :' + os.sep)

    print(inspect.getfile(inspect.currentframe())) # script filename (usually with path)
    print(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))) # script directory
    return

def clean():
    if os.path.exists(_get_in_dir_path()):
        shutil.rmtree(_get_in_dir_path())
    if os.path.exists(_get_out_dir_path()):
        shutil.rmtree(_get_out_dir_path())

clean()
# create_ou_dir()
# create_out_dir()
# test_make_files()
# get_output_file_path()
# get_file_list_from_in_dir()