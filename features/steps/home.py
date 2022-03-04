from behave import given, when, then

@given(u'I navigate to the home page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/')

@when(u'I click on the "i\'m feeling lucky" button')
def step_impl(context):
    context.browser.find_element_by_id("random").click()

@then(u'I should see an artist\'s details page')
def step_impl(context):
    assert 'Number of Tracks in Database:' in context.browser.page_source
    assert 'MusicBrainz' in context.browser.page_source