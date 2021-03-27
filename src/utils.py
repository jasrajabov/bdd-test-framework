import os
from collections import defaultdict
import xml.etree.ElementTree as Xet
import pandas as pd

def file_and_path_finder(path):

    d = defaultdict(lambda: None)

    files = os.scandir(path)
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

            d[str(num)] = {'path': new_path, 'name': file.name}
            os.rename(file.path, new_path)
    return d


def delete_file(file):
    return os.remove(file)


def parse_xml(file):
    xmlparse = Xet.parse(file)
    root = xmlparse.getroot()
    data = {
        'id_type': root[0].find('type').text,
        'id_value': root[0].find('type').text,
        'name': root[1].text,
        'lastname': root[2].text
    }

    return data

def create_csv_file(data, path):
    data = pd.DataFrame([data])
    data.to_csv(path, index=False)


def path_creator(folder_name):
    path = os.path.expanduser(f"~/{folder_name}")
    return path

def isXml(filename):
    return filename.endswith('.xml')
