from behave import when, then, given
from playwright.sync_api import expect
from pages.base_page import StartPage
import time




@given(u'användare är på Lägg till bok sidan')
def step_given_start_page(context):
    context.page.goto(context.base_url)
    context.start_page = StartPage( context.page )


@when(u'användare fyller i fälten The Hobbit och J.R.R. Tolkien')
def step_when_type_book(context):
    # context.page.get_by_test_id('add-input-title').fill('The Hobbit')
    # context.page.get_by_test_id('add-input-author').fill('J.R.R. Tolkien')
    context.start_page.add_book("J.R.R Tolkien", "The Hobbit")



@then(u'boken som användare fyller i fälten ska visas i Katalog-sidan')
def step_add_new_book_visible(context):
    expect(context.start_page.get_book("The Hobbit")).to_be_visible()


#### --- bekräfta kan inte lämna tomt fält --- ####

@given(u'användare är på Lägg till bok sidan2')
def step_given_start_page2(context):
    context.page.goto(context.base_url)
    context.page.get_by_test_id('add-book').click(timeout=500)


@when(u'användare fyller i fälet <Titel> med "The Hobbit"  men lämnar <Författare> tomt')
def step_add_new_book_with_blank_data(context):
    context.page.get_by_test_id('add-input-title').fill('The Hobbit')
    context.page.get_by_test_id('add-input-author').fill('')


@then(u'användare kan inte att trycka på Lägg till ny bok-knappen')
def step_then_button_is_disabled(context):
    button = context.page.get_by_test_id("add-submit")
    expect(button).to_be_disabled()