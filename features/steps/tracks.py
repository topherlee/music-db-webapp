from behave import given, when, then
from selenium.webdriver.support.ui import Select

@given(u'I navigate to the tracks page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/tracks')

@when(u'I filter by year 2000 and track title Y')
def step_impl(context):
    select = Select(context.browser.find_element_by_id("year"))
    select.select_by_value("2000")
    context.browser.find_element_by_xpath("//input[@name='letter'][25]").click()
    context.browser.find_element_by_id("submit").click()
  
@then(u'I should see the track Yellow by Coldplay')
def step_impl(context):
    assert 'Yellow' in context.browser.page_source
    assert 'Coldplay' in context.browser.page_source
    assert 'Tracklist - LOLlingStone' in context.browser.title