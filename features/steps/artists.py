from behave import given, when, then

@given(u'I navigate to the artists page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/artists')

@when(u'I click on the Adam Lambert hyperlink')
def step_impl(context):
    context.browser.find_element_by_link_text("Adam Lambert").click()

@then(u'I should see Adam Lambert\'s details page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/artist_details/ARIGTAO11FED0C4411'
    assert 'Number of Tracks in Database:' in context.browser.page_source
    assert 'Adam Lambert' in context.browser.page_source