from behave import when, then, given
from playwright.sync_api import expect, sync_playwright
from pages.base_page import StartPage, toggle_favorite
import time


@given(u'Jag öppnar webbplatsen')
def step_given_open_webpage(context):
    context.start = time.time()
    context.page.goto(context.base_url)
    context.end = time.time()


@then(u'Laddningstiden ska vara under 3 sekunder')
def step_then_be_fast(context):
    assert (context.end - context.start) < 3


###### firefox test #####

@given(u'Jag öppnar webbplatsen med firefox')
def step_given_use_firefox(context):
    context.page.goto(context.base_url)


@then(u'Sidan ska renderas korrekt')
def step_then_it_works(context):
    toggle_favorite(context.page, 'Min katt är min chef')
    context.page.get_by_test_id('favorites').click(timeout=500)
    result = context.page.get_by_test_id('fav-Min katt är min chef')
    expect(result).to_be_visible()
