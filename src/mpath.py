import os
import inspect


def main_dir():
    # the os.getcwd return the path of the scrip of the execute
    dir_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    return dir_path


'''
def test_path():
    print(inspect.getfile(inspect.currentframe()))  # script filename (usually with path)
    print(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))  # script directory
'''
