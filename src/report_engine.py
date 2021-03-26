from src.utils import file_and_path_finder, parse_xml, delete_file, create_csv_file, path_creator
import xml.etree.ElementTree as Xet
import datetime



class ReportGenerator():

    def __init__(self):
        try:
            self.output_file_path = path_creator('Desktop/output_files')
        except:
            raise FileNotFoundError('Folder does not exist!')



    def handle_files(self):
        files = file_and_path_finder()
        if files:
            print('Found file to parse! Parsing...')
        else:
            print('No file to parse...')
        for each_file in files:
            file = files[each_file]
            parsed = parse_xml(file['path'])
            create_csv_file(parsed, f'{self.output_file_path}/file_{datetime.datetime.utcnow()}.csv')
            # delete_file(file['path'])

    def run(self):
        return self.handle_files()




