import os
from collections import defaultdict
import xml.etree.ElementTree as Xet
import pandas as pd

def file_and_path_finder(path):

    _dict = defaultdict(lambda: None)

    files = scand_dir(path)
    for data in enumerate(files):
        num = data[0]
        file = data[1]
        if all([
                file.is_file(),
                not file.name.startswith('parsed'),
                isXml(file.name)
        ]):
            """this will replace filename to parsed"""
            splitted = file.path.split('/')
            splitted[-1] = 'parsed_' + splitted[-1]
            new_path = "/".join(splitted)

            _dict[str(num)] = {'path': new_path, 'name': file.name}
            os.rename(file.path, new_path)
    return _dict


def delete_file(file):
    if os.path.isfile():
        return os.remove(file)


def parse_xml(file):

    data = None
    """
    root[0] - <tx>
                </tx>
    """
    try:
        xmlparse = Xet.parse(file)
        root = xmlparse.getroot()
        data = {
            'id_type': root[0][0].find('type').text,
            'id_value': root[0][0].find('value').text,
            'name': root[0][1].text,
            'lastname': root[0][2].text
        }
    except:
        raise Xet.ParseError('Failed to parse xml!')

    return data

def create_csv_file(data, path):
    data = pd.DataFrame([data])
    data.to_csv(path, index=False)


def path_creator(folder_name):
    path = os.path.expanduser(f"~/{folder_name}")
    return path

def isXml(filename):
    return filename.endswith('.xml')

def scand_dir(path):
    """
    :param path: folder to be scanned
    :return: list of file objects in the folder
    """
    return os.scandir(path)
