from behave import given, when, then, use_step_matcher


use_step_matcher('re')


@given(r'that I am logged in as professor "[^"]+"')
def step_impl(context):
    raise NotImplementedError('Professor/Course management')


@given(r'"[^"]+" does not exist')
def step_impl(context):
    pass


@when(r'I attempt to create a course "[^"]+"')
def step_impl(context):
    pass


@then(r'course "[^"]+" exixts')
def step_impl(context):
    pass


@then(r'course "[^"]+" has no dependents')
def step_impl(context):
    pass


@given(r'course "[^"]+" exists')
def step_impl(context):
    pass


@when(r'I attempt to add a new assessment "[^"]+" to course "[^"]+"')
def step_impl(context):
    pass


@then(r'"[^"]+" exists and is open')
def step_impl(context):
    pass


@then(r'"[^"]+" is associated with "[^"]+"')
def step_impl(context):
    pass


@given(r'"[^"]+" exixts and is open')
def step_impl(context):
    pass


@given(r'"[^"]+" is associated with "[^"]+"')
def step_impl(context):
    pass


@given(r'"[^"]+" has at least "[^"]+" submission')
def step_impl(context):
    pass


@when(r'I attemp to grade "[^"]+"')
def step_impl(context):
    pass


@then(r'"[^"]+" is graded and closed')
def step_impl(context):
    pass


@then(r'studnets who submitted "[^"]+" are sent a notification')
def step_impl(context):
    pass
