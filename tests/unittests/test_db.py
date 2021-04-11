import mock
import pytest
from src.db_manager import dbManager
import psycopg2



@mock.patch('src.db_manager.psycopg2.connect')
@mock.patch('src.db_manager.time')
@mock.patch('src.db_manager.db_config')
def test_db_retry(mock_config, mock_time, mock_psycopg2):
    mock_time.sleep.return_value = None
    mock_psycopg2.side_effect = psycopg2.DatabaseError()
    mock_config.return_value = {'test':'test'}
    with pytest.raises(psycopg2.DatabaseError):
        dbManager().db_connect_retry()

    assert mock_psycopg2.call_count == 3


@mock.patch('src.db_manager.psycopg2')
@mock.patch('src.db_manager.db_config')
def test_db_retry_connection_successful(mock_config, mock_psycopg2):
    mock_psycopg2.sleep.return_value = None
    mock_config.return_value = {'test': 'test'}
    conn = dbManager().db_connect_retry()
    assert conn is not None

@mock.patch('src.db_manager.dbManager.db_connect_retry')
def test_db_connect(mock_retry):
    mock_retry.side_effect = psycopg2.DatabaseError()
    with pytest.raises(psycopg2.DatabaseError):
        dbManager().connect_to_db()

@mock.patch('src.db_manager.dbManager.db_connect_retry')
def test_create_table(mocked_conn):
    _mock = mock.Mock()
    mocked_conn().cursor.return_value = _mock
    _mock.execute.return_value = None
    dbManager().create_table()



    mocked_conn.assert_called()
    _mock.execute.assert_called_once()
    _mock.execute.assert_called_with("""CREATE TABLE REPORT (TX_ID SERIAL PRIMARY KEY,
                                                ID_TYPE VARCHAR(255) NOT NULL,
                                                ID_VALUE VARCHAR(255) NOT NULL,
                                                NAME VARCHAR(255) NOT NULL,
                                                LASTNAME VARCHAR(255) NOT NULL)""")
    mocked_conn().commit.assert_called_once()
    _mock.close.assert_called_once()



