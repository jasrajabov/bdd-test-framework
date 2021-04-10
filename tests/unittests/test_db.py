import mock
from src.db_commands import *
import pytest
from src.db_manager import connect_to_db
import psycopg2

@mock.patch('src.db_commands.psycopg2.connect')
@mock.patch('src.db_commands.time')
def test_db_retry(mock_time, mock_psycopg2):
    mock_time.sleep.return_value = None
    mock_psycopg2.side_effect = psycopg2.DatabaseError()
    with pytest.raises(psycopg2.DatabaseError):
        db_connect_retry(**{'test':'test'})

    assert mock_psycopg2.call_count == 3


@mock.patch('src.db_commands.psycopg2')
def test_db_retry_connection_successful(mock_psycopg2):
    mock_psycopg2.sleep.return_value = None
    conn = db_connect_retry(**{'test':'test'})
    assert conn is not None

@mock.patch('src.db_manager.db_connect_retry')
def test_db_connect(mock_retry):
    mock_retry.side_effect = psycopg2.DatabaseError()
    with pytest.raises(psycopg2.DatabaseError):
        connect_to_db()
