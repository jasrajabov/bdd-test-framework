import mock
from unittest.mock import Mock
from config import *


@mock.patch('config.isTestEnv')
def test_config_env(mock_testEnv):
    mock_testEnv.return_value = True
    conf = db_config()
    assert conf['database']  == 'reportdb_test'


def test_conf():
    mock = Mock(name='mock_conf')
    mock.isTestEnv.return_value = False
    conf = db_config()
    assert conf['database'] == 'reportdb'

@mock.patch('config.os.environ')
def test_isTestEnv(mock_os):
    isTestEnv()
    mock_os.get.assert_called()

