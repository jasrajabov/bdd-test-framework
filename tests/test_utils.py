import shutil
import os
from src.utils import path_creator, file_and_path_finder

def copy_file_to_dest(source, destination):
    if not destination:
        raise TypeError('Missing destination path!')

    test_files_source = path_creator(source)
    destination_path = path_creator(destination)

    files = file_and_path_finder(test_files_source)
    list_of_file_names = []
    for file in files:
        test_file_path = file['path']
        shutil.copyfile(test_file_path, destination_path)
        list_of_file_names.append(file['name'])

    return list_of_file_names

def report_presence_check(path):
    res = []
    path = path_creator(path)
    files = os.scandir(path)
    for data in enumerate(files):
        num = data[0]
        file = data[1]
        if all([
                file.is_file(),
                file.name.endswith('.csv'),

        ]):
            res.append(file.name)
    return res
