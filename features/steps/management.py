from behave import given, when, then, use_step_matcher


use_step_matcher('re')


@given(u'that I am logged in as general staff "userstaff"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given that I am logged in as general staff "userstaff"')


@given(u'user "user1" does not exist')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given user "user1" does not exist')


@when(u'I attempt to add new user "user1" with role "student"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I attempt to add new user "user1" with role "student"')


@then(u'user "user1" exixts with role "student"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user "user1" exixts with role "student"')


@given(u'user "user1" exixts with role "student"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given user "user1" exixts with role "student"')


@when(u'I attempt to send an invoice to user "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I attempt to send an invoice to user "user1"')


@then(u'user "user1" recieves an invoice')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user "user1" recieves an invoice')
