import psycopg2
from config import db_config
import logging
from src.db_commands import db_connect_retry

logger = logging.getLogger(__name__)

def connect_to_db():

    conn =  None
    params = db_config()
    conn = db_connect_retry(**params)
    if conn:
        db_info = conn.info

        logger.info(f'Connected to a db. DSN parameters: {db_info.dsn_parameters}')
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

        # close the communication with the PostgreSQL
        cur.close()

    if conn is not None:
        conn.close()
        logger.info('Database connection closed!')
