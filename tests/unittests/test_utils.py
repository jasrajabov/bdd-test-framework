import unittest
import mock
from src.utils import scand_dir, file_and_path_finder, isXml, parse_xml, Xet, delete_file, path_creator
from dicttoxml import dicttoxml

class TestUtils(unittest.TestCase):

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
        self.assertEqual(d, {"0":{"path":"folder/parsed_test.xml", "name": "test.xml"}})

    def test_isXml(self):
        self.assertTrue(isXml('test.xml'))

    def test_parse_xml_raises_ParseError(self):
        xml = dicttoxml({'test':'test'})
        xml_test = xml.decode()
        with self.assertRaises(Xet.ParseError):
            parse_xml(xml_test)

    @mock.patch('src.utils.Xet')
    @mock.patch('src.utils.parse_xml')
    def test_parse_xml_parses_xml(self, mocked_xml, mock_parse_xml):
        """
        :description: Did not wanna save xml in an actual place, therefore mocked xml lib to parse from string"
        :param mocked_xml: mocking xml library
        :param mock_parse_xml: and mocking xml_parse_mehtod
        :return:
        """
        data = {"tx":
            {
                "id": {
                    "type": "random",
                    "value": "abc"
                },
                "name": "H",
                "lastname": "Pk"

            }
        }
        xml = dicttoxml(data)
        xml_test = xml.decode()
        mocked_xml.parse.return_value = Xet.fromstring(xml_test)
        mock_parse_xml.root.return_value = mocked_xml.parse
        self.assertIsNotNone(parse_xml(xml_test))

    @mock.patch('src.utils.os')
    def test_delete_file(self, mock_os):
        mock_os.path.isfile.return_value = True
        delete_file('file')
        self.assertTrue(mock_os.remove.called, "Removed even if not isfile()")
        mock_os.remove.assert_called_once()


    def test_create_path(self):
        path = path_creator('/test')
        self.assertTrue(path.endswith('/test'))







