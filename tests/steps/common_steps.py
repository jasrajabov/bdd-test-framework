from behave import given, when, then
from src.report_engine import ReportGenerator


@given(u'App is launched')
def step_impl(context):
    context.app = ReportGenerator()
    pass


@when(u'xml file is present in the input folder')
def step_impl(context):
    pass


@then(u'xml parser parses the file')
def step_impl(context):
    pass
