from behave import given, when, then, use_step_matcher


use_step_matcher('re')


@given(r"that I am a student")
def step_impl(context):
    pass


@given(r'I am on the home page')
def step_impl(context):
    pass


@given(r'my (?:invalid )?credentials are username "(?P<username>[^"]+)" and password "(?P<password>[^"]+)"')
def step_impl(context, username, password):
    context.credentials = {'username': username, 'password': password}


@when(r'I enter my credentials into the login form')
def step_impl(context):
    credentials = context.credentials
    context.browser.find_element_by_id('username').send_keys(credentials['username'])
    context.browser.find_element_by_id('password').send_keys(credentials['password'])


@when(r'I submit the form')
def step_impl(context):
    context.browser.find_element_by_id('submit').click()


@then(r'I should be redirected to the student homepage')
def step_impl(context):
    assert 'Student Homepage' in context.browser.page_source


@then(r'I should remain on the logged-out homepage')
def step_impl(context):
    assert 'Login' in context.browser.page_source


@then(r'I should see an error message that reads "(?P<msg>[^"]+)"')
def step_impl(context, msg):
    assert msg in context.browser.page_source
