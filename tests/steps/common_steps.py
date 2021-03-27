from behave import given, when, then
from src.report_engine import ReportGenerator
from tests.test_utils import copy_file_to_dest, file_and_path_finder, path_creator, report_presence_check


@given(u'following paths')
def step_impl(context):
    context.test_file_path = context.table[0]['input_path']
    context.output_files_path = context.table[0]['output_path']

@when(u'App is launched')
def step_impl(context):
    context.app = ReportGenerator(context.test_file_path, context.output_files_path)
    context.app.run()

@when(u'xml file is copied from input_path into output_path folder')
def step_impl(context):
    context.list_of_files_copied = copy_file_to_dest(context.test_file_path, context.output_files_path)

@then(u'xml parser parses the file and generates {report}')
def step_impl(context, report):
    context.output_file_name = report
    data = report_presence_check(context.output_files_path)
    assert context.output_file_name in data