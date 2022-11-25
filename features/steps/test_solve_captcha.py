from behave import given, when, then
from captcha_solver import CaptchaSolver
import os.path

@given('{image} como captcha')
def step_impl(context, image):
    context.solver = CaptchaSolver('YOUR API KEY')
    context.file_path = os.path.join('features', 'files', image)

@when('se pide resolver el captcha')
def step_impl(context):
    context.result = context.solver.resolve(context.file_path)

@then('el resultado es {response}')
def step_impl(context, response):
    if response != 'error':
        assert context.result == response
    else:
        return isinstance(context.result, str)