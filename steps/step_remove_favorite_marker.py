from asyncio import timeout
from behave import when, then, given
from playwright.sync_api import expect
from pages.base_page import StartPage, toggle_favorite

@given(u'användaren är på startsidan med två sparade favoritböcker2')
def step_given_user_at_start_page_with_favorites(context):
    context.page.goto(context.base_url)
    toggle_favorite(context.page, 'Min katt är min chef')
    toggle_favorite(context.page, 'Hur man tappar bort sin TV-fjärr 10 gånger om dagen')


@given(u'böckerna "Min katt är min chef" och "Hur man tappar bort sin TV-fjärr 10 gånger om dagen" visas i favoritlistan')
def step_verify_given1(context):
    context.page.get_by_test_id('favorites').click(timeout=500)
    saved_favorite = context.page.locator('[data-testid="book-list"] > li')
    expect(saved_favorite).to_have_count(2)


@when(u'användaren klickar på ta bort-favorit-knappen för "Min katt är min chef"')
def step_when_remove_favorites(context):
   context.page.get_by_test_id('catalog').click(timeout=500)
   context.page.get_by_test_id('star-Min katt är min chef').click(timeout=500)


@then(u'"Min katt är min chef" ska inte längre visas i favoritlistan')
def step_verify_have_only_1_fav(context):
    context.page.get_by_test_id('favorites').click(timeout=500)
    saved_favorites = context.page.locator('[data-testid="book-list"] > li')
    expect(saved_favorites).to_have_count(1)


@then(u'"Hur man tappar bort sin TV-fjärr 10 gånger om dagen" ska fortfarande finnas kvar')
def step_favorite_book_visible(context):
    remaining_fav = context.page.get_by_text('Hur man tappar bort sin TV-fjärr 10 gånger om dagen')
    expect(remaining_fav).to_be_visible()


