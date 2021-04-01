import logging

format_string = "%(asctime)s: %(levelname)s: %(funcName)s line:%(lineno)d %(message)s"

logging.basicConfig(
    filename='/Users/jasurbek/Desktop/python_projects/draft/logfiles/app.log',
    level=logging.DEBUG,
    filemode="a",
    format=format_string
)