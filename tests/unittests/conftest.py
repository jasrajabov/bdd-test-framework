import pytest


@pytest.fixture(scope='function')
def sample_dict():
    """

    :return: yields pass values to dynamically use fixture
    """
    test_dict = {"tx":
        {
            "id": {
                "type": "random",
                "value": 'asd'
            },
            "name": "H",
            "lastname": "Pk"
        }
    }

    def pass_values(k=None, v=None):
        """

        :param k: key name of test_dict
        :param v: value of key
        :return: returns test_dict as above or with new values
        """
        if not k:
            return test_dict
        if test_dict['tx'][k]:
            test_dict['tx'][k]=v

        return test_dict
    yield pass_values