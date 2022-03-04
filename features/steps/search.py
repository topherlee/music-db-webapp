from behave import given, when, then

@given(u'I navigate to the search page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/search')

@when(u'I click and type on the search box')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/search'
    context.browser.find_element_by_name("query").send_keys("the white stripes")
    context.browser.find_element_by_id("artist").click()
    context.browser.find_element_by_id("submit").click()

@when(u'I click on this specific hyperlink')
def step_impl(context):
    context.browser.find_element_by_link_text('The White Stripes').click()
    
@then(u'I should see the artist details page')
def step_impl(context):
    assert 'Seven Nation Army' in context.browser.page_source
    assert context.browser.title == 'The White Stripes - Artist Details - LOLlingStone'