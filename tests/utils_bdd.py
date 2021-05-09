import shutil
import os
from src.utils import path_creator, file_and_path_finder

def copy_file_to_dest(source, destination):
    """
    :param source: path of the source file to be copied from
    :param destination: path of the destination files to be copied to
    :return: returns list of files that were copied
    """
    if not destination:
        raise TypeError('Missing destination path!')

    files = file_and_path_finder(source)
    list_of_file_names = []
    for file in files:
        test_file_path = file['path']
        shutil.copyfile(test_file_path, destination)
        list_of_file_names.append(file['name'])

    return list_of_file_names

def report_presence_check(path):

    """
    :param path: path you to be checked
    :return: returns list of csv files in the folder
    :TODO: we can enhance it to take any file
    """

    res = []
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


from dicttoxml import dicttoxml
def dict_to_xml(dict, filename, dest_folder):

    """
    :param dict: takes a dictionary to be converted for xml
    :param filename: filename you want xml to be saved as
    :param dest_folder: destination folder
    :return: saves xml file in the folder and returns xml file
    """

    xml = dicttoxml(dict)
    xml_decode = xml.decode()
    xmlfile = open(f'{dest_folder}/{filename}', "w")
    xmlfile.write(xml_decode)
    xmlfile.close()
    return xml

