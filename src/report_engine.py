from src.utils import *
import logging
import time
from src.db_manager import dbManager
from config import ROOT_DIR

logger = logging.getLogger(__name__)

db = dbManager()
class ReportGenerator():

    def __init__(self, input_path, output_path):
        """
        TODO: REMOVE THIS TEMPORARY FIX TO PASS ACCEPTANCE TESTS
        :param input_path:
        :param output_path:
        """

        ###TEMPORARY WORKAROUND TO FIX TESTS
        self.output_file_path = output_path
        self.input_file_path = input_path
        if not check_if_folder_exists(input_path) and check_if_folder_exists(output_path):
            self.output_file_path = path_creator(output_path)
            self.input_file_path = path_creator(input_path)
            ### END
            if check_if_folder_exists(self.output_file_path) and check_if_folder_exists(self.input_file_path):
                logger.info(f'Paths: Input: {self.output_file_path} Output: {self.input_file_path} paths were passed!')
                db.connect_to_db()
            else:
                logger.warning(f'{self.input_file_path} or {self.output_file_path} do not exist. Creating folders in root')
                self.output_file_path = ROOT_DIR + '/OUTPUT_FILES'
                self.input_file_path = ROOT_DIR + '/INPUT_FILES'
                if not check_if_folder_exists(self.output_file_path) and check_if_folder_exists(self.input_file_path):
                    os.mkdir(self.output_file_path)
                    os.mkdir(self.input_file_path)
                db.connect_to_db()


    def handle_files(self):
        files = None
        allowance = 5
        try:
            files = file_and_path_finder(self.input_file_path)
        except FileNotFoundError:
            while allowance != 0:
                logger.error(f'{self.output_file_path} or {self.input_file_path} folders do not exist! Retrying.... {allowance} retries left!')
                allowance -= 1
                time.sleep(2)
                if allowance == 0:
                    logger.error('Maximum retries have been reached! Termination session!')
                    raise RuntimeError

        if files:
            logger.info('Found file to parse! Parsing...')
            for each_file in files:
                file = files[each_file]
                parsed = parse_xml(file['path'])
                db.insert_db_record(parsed)
                create_csv_file(parsed, f'{self.output_file_path}/reportFile_{file["name"].split(".")[0]}.csv')
        else:
            logger.info('No file to parse...')


    def run(self):
        return self.handle_files()




