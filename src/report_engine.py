from src.utils import *
import logging
import time
from src.db_manager import connect_to_db

logger = logging.getLogger(__name__)

class ReportGenerator():

    def __init__(self, input_path, output_path):
        self.output_file_path = path_creator(output_path)
        self.input_file_path = path_creator(input_path)
        logger.info(f'Paths: Input: {self.output_file_path} Output: {self.input_file_path} paths were passed!')
        connect_to_db()
        logger.info('Successfully connected to DB!')


    def handle_files(self):
        files = None
        allowance = 5
        try:
            files = file_and_path_finder(self.input_file_path)
        except FileNotFoundError:
            while allowance != 0:
                logger.error(f'{self.output_file_path} or {self.input_file_path} folders do not exist! Retrying.... {allowance} retries left!')
                allowance -= 1
                time.sleep(5)
                if allowance == 0:
                    logger.error('Maximum retries have been reached! Termination session!')
                    raise RuntimeError

        if files:
            logger.info('Found file to parse! Parsing...')
            for each_file in files:
                file = files[each_file]
                parsed = parse_xml(file['path'])
                create_csv_file(parsed, f'{self.output_file_path}/reportFile_{file["name"].split(".")[0]}.csv')
        else:
            logger.info('No file to parse...')


    def run(self):
        return self.handle_files()




