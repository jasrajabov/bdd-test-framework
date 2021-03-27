from src.utils import file_and_path_finder, parse_xml, delete_file, create_csv_file, path_creator
import xml.etree.ElementTree as Xet
import datetime



class ReportGenerator():

    def __init__(self, input_path, output_path):
        try:
            self.output_file_path = path_creator(output_path)
            self.input_file_path = path_creator(input_path)
        except:
            raise FileNotFoundError('Folder does not exist!')



    def handle_files(self):
        files = file_and_path_finder(self.input_file_path)
        if files:
            print('Found file to parse! Parsing...')
        else:
            print('No file to parse...')
        for each_file in files:
            file = files[each_file]
            parsed = parse_xml(file['path'])
            create_csv_file(parsed, f'{self.output_file_path}/reportFile_{file["name"].split(".")[0]}.csv')
            # delete_file(file['path'])

    def run(self):
        return self.handle_files()




