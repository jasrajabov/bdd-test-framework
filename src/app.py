from report_engine import ReportGenerator
import time
from logfiles.log import logging

app = ReportGenerator('Desktop/ftp-files', 'Desktop/output_files')

interval = 5

if __name__ == "__main__":
    while True:
        logging.info('App has started running')
        app.run()
        logging.info(f'Putting into sleep for {interval} seconds')
        time.sleep(interval)
        logging.info(f'Rerunning app')

