import psycopg2
from config import db_config
import logging

import time

logger = logging.getLogger(__name__)


class dbManager():

    def __init__(self):
        self.params = db_config()

    def connect_to_db(self):

        conn = None
        conn = self.db_connect_retry()
        if conn:
            db_info = conn.info
            logger.info(f'Connected to a db. DSN parameters: {db_info.dsn_parameters}')
            self.create_table()


        if conn is not None:
            conn.close()
            logger.info('Database connection closed!')

    def db_connect_retry(self):
        conn = None
        retry = 3
        while retry != 0:
            try:
                conn = psycopg2.connect(**self.params)
                if conn:
                    print('Connection was successful!')
                    return conn
            except:
                retry -= 1
                time.sleep(2)
                print('Failed to connect! Retrying....')
        raise psycopg2.DatabaseError()

    def create_table(self):

        conn = self.db_connect_retry()
        cur = conn.cursor()
        try:
            cur.execute("""CREATE TABLE REPORT (TX_ID SERIAL PRIMARY KEY,
                                                ID_TYPE VARCHAR(255) NOT NULL,
                                                ID_VALUE VARCHAR(255) NOT NULL,
                                                NAME VARCHAR(255) NOT NULL,
                                                LASTNAME VARCHAR(255) NOT NULL)""")
            conn.commit()
            logger.info('Table is created successfully')
        except Exception as e:
            logger.warning(e)
        cur.close()

    def insert_db_record(self, data):
        conn = self.db_connect_retry()
        cur = conn.cursor()
        try:
            query = """INSERT INTO REPORT (TX_ID, ID_TYPE, ID_VALUE, NAME, LASTNAME) VALUES (%s,%s,%s,%s,%s,)"""
            record_to_insert = set()
            for key in data:
                record_to_insert.add(data[key])

            cur.execute(query, record_to_insert)

            conn.commit()
            count = cur.rowcount
            logger.info(count, "Record inserted successfully into mobile table")

        except (Exception, psycopg2.Error) as error:
            logger.error(error)