from report_engine import ReportGenerator
import time

app = ReportGenerator()




if __name__ == "__main__":
    while True:
        print('Running!')
        app.run()
        time.sleep(5)
        print('Re-running!')

