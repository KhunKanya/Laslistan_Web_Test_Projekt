from behave import when, then, given
from playwright.sync_api import expect
from pages.base_page import StartPage
import time


######## Add favourite marker ########


@given(u'Användaren är på startsidan')
def step_given_at_startpage(context):
    context.page.goto(context.base_url)
    context.start_page = StartPage( context.page )


@when(u'änvändare klickar på favorit-knappen för Min katt är min chef')
def step_when_click_favourite_cat(context):
    context.start_page.toggle_favorite('Min katt är min chef')


@then(u'ska boken Min katt är min chef finnas i mina böcker-sidan')
def step_then_be_fav(context):
    context.page.get_by_test_id('favorites').click(timeout=500)
    result = context.page.get_by_test_id('fav-Min katt är min chef')
    # time.sleep(5)
    expect(result).to_be_visible()


@when(u'änvändare klickar på favorit-knappen för Hur man tappar bort sin TV-fjärr 10 gånger om dagen')
def step_when_add_remote_fav(context):
    context.page.goto(context.base_url)
    context.start_page = StartPage(context.page)
    context.start_page.toggle_favorite('Hur man tappar bort sin TV-fjärr 10 gånger om dagen')


@then(u'ska boken Hur man tappar bort sin TV-fjärr 10 gånger om dagen finnas i mina böcker-sidan')
def step_then_have_one_more_fav(context):
    context.start_page.get_button('favorites').click(timeout=200)
    result2 = context.page.get_by_test_id('fav-Hur man tappar bort sin TV-fjärr 10 gånger om dagen')
    expect(result2).to_be_visible()


