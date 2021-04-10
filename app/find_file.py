import os
import cfgs


def find_files_by_dirctory(dirctory,prefix=''):
    res = os.listdir(dirctory)
    for i in range(len(res)):
        res[i] = prefix+res[i]
    return res


def get_file_path(dirctory):
    for i in range(len(dirctory)):
        if dirctory[-i-1] == '/':
            return dirctory[:-i-1]
    return ''


def get_file_name(dirctory):
    for i in range(len(dirctory)):
        if dirctory[-i-1] == '/':
            return dirctory[-i:]
    return dirctory

"""
test_str='/home/johnny/project/test_project/flask/test_dir/tinypilot'

print(get_file_name(test_str))
print(get_file_path(test_str))
"""