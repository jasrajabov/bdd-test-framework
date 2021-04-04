import mock
from src.utils import *
from dicttoxml import dicttoxml
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

class TestUtils:

    @mock.patch('src.utils.os')
    def test_scandir(self, mock_os):
        scand_dir('any folder')
        #test scand_dir is called with right params
        mock_os.scandir.assert_called_with('any folder')


    @mock.patch('src.utils.scand_dir')
    @mock.patch('src.utils.os')
    def test_file_and_path_handler(self, mock_os, mock_scand_dir ):

        mock_scand_dir.name = 'test.xml'
        mock_scand_dir.is_file.return_value = True
        mock_scand_dir.path = 'folder/test.xml'
        mock_scand_dir.return_value = [mock_scand_dir]
        d = file_and_path_finder('any folder')
        assert d == {"0":{"path":"folder/parsed_test.xml", "name": "test.xml"}}

    def test_isXml(self):
        assert isXml('test.xml')

    def test_parse_xml_raises_ParseError(self):
        xml = dicttoxml({'test':'test'})
        xml_test = xml.decode()
        with pytest.raises(Xet.ParseError) as err:
            parse_xml(xml_test)

        assert err.value.__str__() == 'Failed to parse xml!'


    def test_parse_xml_raises_ValueError(self, sample_dict):
        test_dict = sample_dict(k='name', v='J')
        xml = dicttoxml(test_dict)
        xml_test = xml.decode()
        file = save_as_file(xml_test, 'test_data_1', 'xml', '/Users/jasurbek/Desktop/python_projects/draft/tests/test_data')
        with pytest.raises(ValueError) as err:
            parse_xml(file.name)

        assert err.value.__str__() == 'Id value is not integer and cannot be none!'

    @mock.patch('src.utils.Xet')
    @mock.patch('src.utils.parse_xml')
    def test_parse_xml_parses_xml(self, mocked_xml, mock_parse_xml, sample_dict):
        """
        :description: Did not wanna save xml in an actual place, therefore mocked xml lib to parse from string"
        :param mocked_xml: mocking xml library
        :param mock_parse_xml: and mocking xml_parse_mehtod
        :return:
        """
        data = sample_dict()
        xml = dicttoxml(data)
        xml_test = xml.decode()
        mocked_xml.parse.return_value = Xet.fromstring(xml_test)
        mock_parse_xml.root.return_value = mocked_xml.parse
        assert parse_xml(xml_test) is not None

    @mock.patch('src.utils.os')
    def test_delete_file(self, mock_os):
        mock_os.path.isfile.return_value = True
        delete_file('file')
        assert mock_os.remove.called
        mock_os.remove.assert_called_once()


    def test_create_path(self):
        path = path_creator('/test')
        assert path.endswith('/test')

    def test_integer_value(self):
        assert validate_integer('123')







