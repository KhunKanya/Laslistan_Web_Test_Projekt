from asyncio import timeout
from behave import when, then, given
from playwright.sync_api import expect
from pages.base_page import StartPage, toggle_favorite
import re

@given(u'användaren öppnar Mina böcker-sidan utan sparade favoritböcker')
def step_given_at_empty_start_page(context):
    context.page.goto(context.base_url)
    context.start_page = StartPage(context.page)

@then(u'ska ett meddelande visas: "När du valt, kommer dina favoritböcker att visas här."')
def step_then_show_message(context):
    context.start_page.get_button('favorites').click(timeout=500)
    # message = context.page.get_by_text('När du valt, kommer dina favoritböcker att visas här.')
    message = context.page.get_by_text(re.compile('När du.+favoritböcker'))
    expect(message).to_be_visible()


@when(u'Användaren lägger till en favoritbok')
def step_when_add_new_fav(context):
    context.start_page.get_button('catalog').click(timeout=500)
    context.start_page.toggle_favorite('100 sätt att undvika måndagar')


@then(u'Ovan meddelande syns ej längre')
def step_then_verify_no_message(context):
    context.start_page.get_button('favorites').click(timeout=500)
    message = context.page.get_by_text(re.compile('När du.+favoritböcker'))
    expect(message).not_to_be_visible()
