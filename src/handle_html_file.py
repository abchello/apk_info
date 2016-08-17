#-*_coding:utf8-*-
import inspect
import os
import shutil
from bs4 import BeautifulSoup

#Get test file path
def get_file_path():

    test_file_path = ''

    # the test dirs
    test_dir = os.path.join(os.getcwd(), 'test_file')

    # traverse the test dirs
    list_dirs = os.walk(test_dir)
    is_find_file = False
    for root, dirs, files in list_dirs:
        if is_find_file:
            break
        for f in files:
            file_path = os.path.join(root, f)
            print(os.path.join(root, f))
            if os.path.isfile(file_path):
                test_file_path = file_path
                is_find_file = True
                break
    print('the file path :' + test_file_path)
    return test_file_path

def explain_html(path):
    soup = BeautifulSoup(open(path, encoding='utf-8'))

get_file_path()