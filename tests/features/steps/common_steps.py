from behave import given, when, then
from src.report_engine import ReportGenerator
from tests.utils_bdd import copy_file_to_dest, file_and_path_finder, path_creator, report_presence_check, \
    dict_to_xml
from src.db_manager import *



@given(u'following paths input_path and output_path')
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


@when(u'test xml {file} is created')
def step_impl(context, file):
    context.test_dict = {"tx":
                             {
                                 "id": {
                                     "type": "random",
                                     "value": 123
                                 },
                                 "name": "H",
                                 "lastname": "Pk"

                             }
                        }
    dict_to_xml(context.test_dict, file, context.test_file_path)

@then(u'xml parser parses the file and generates {report}')
def step_impl(context, report):
    context.output_file_name = report
    data = report_presence_check(context.output_files_path)
    assert context.output_file_name in data


@when(u'test xml {input_file} is created with following details: {name}, {lastname}, {id_type}, {id_value}')
def step_impl(context, input_file, name, lastname, id_type, id_value):
    context.test_dict = {"tx":
        {
            "id": {
                "type": id_type,
                "value": id_value
            },
            "name": name,
            "lastname": lastname

        }
    }
    dict_to_xml(context.test_dict, input_file, context.test_file_path)

@then(u'data is saved in db')
def step_impl(context):
    context.db_manager = dbManager()
    db_query_result = context.db_manager.query_db_record(context.test_dict['tx'])
    assert db_query_result is not None

@given(u'db is up and running')
def step_impl(context):
    conn = context.db_manager = dbManager()
    assert conn is not None