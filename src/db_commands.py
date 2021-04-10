import time
import psycopg2


def db_connect_retry(**kwargs):
    conn = None
    retry = 3
    while retry != 0:
        try:
            conn = psycopg2.connect(**kwargs)
            if conn:
                print('Connection was successful!')
                return conn
        except:
            retry -= 1
            time.sleep(2)
            print('Failed to connect! Retrying....')
    raise psycopg2.DatabaseError()

