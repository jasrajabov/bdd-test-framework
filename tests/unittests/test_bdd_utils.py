import unittest, mock
from tests.utils_bdd import report_presence_check, copy_file_to_dest

class TestBddUtils:

    @mock.patch('tests.utils_bdd.os')
    def test_report_presence_check(self, mock_os):

        mock_os.name = 'test.csv'
        mock_os.is_file.return_value = True
        mock_os.scandir.return_value = [mock_os]
        reports = report_presence_check('any')
        assert reports == ['test.csv']

    @mock.patch('tests.utils_bdd.file_and_path_finder')
    @mock.patch('tests.utils_bdd.shutil')
    def test_copy_files_to_dest(self,  mock_shutil, mock_file_and_path_handler):

        mock_file_and_path_handler.return_value = [{'path': 'path', 'name': 'test'}]
        mock_shutil.copyfile.return_value = None

        files = copy_file_to_dest('test', 'test')
        assert files == ['test']



