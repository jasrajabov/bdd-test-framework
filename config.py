from configparser import ConfigParser
import os

def db_config():
    db = 'DB'
    if isTestEnv():
        db = 'DB_TEST'
    parser = ConfigParser()
    parser.read('/Users/jasurbek/Desktop/python_projects/draft/config.ini')
    conf = {
        'host': parser[db]['host'],
        'database': parser[db]['database'],
        'user': parser[db]['user'],
        'password': parser[db]['password'],
    }
    return conf


def isTestEnv():
    return os.environ.get('TEST')



