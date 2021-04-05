from configparser import ConfigParser

def db_config():

    parser = ConfigParser()
    parser.read('/Users/jasurbek/Desktop/python_projects/draft/config.ini')
    conf = {
        'host': parser['POSTGRESQL']['host'],
        'database': parser['POSTGRESQL']['database'],
        'user': parser['POSTGRESQL']['user'],
        'password': parser['POSTGRESQL']['password'],
    }
    return conf



