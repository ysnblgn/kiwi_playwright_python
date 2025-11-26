import re
from playwright.sync_api import expect, Page
from pytest_bdd import given,when,then,parsers


@given(parsers.parse('As an not logged user I navigate to homepage "{url}"'))
def navigate_home(home, url):
    home.open(url)
    home.accept_cookies()

@when("I select one-way trip type")
def select_one_way_trip(home):
    home.select_one_way_trip()

@when(parsers.parse('Set as departure airport "{code}"'))
def set_airport(home, code):
    home.set_airport(code, "departure")

@when(parsers.parse('Set as arrival airport "{code}"'))
def set_airport(home, code):
    home.set_airport(code, "arrival")

@when(parsers.cfparse('Set the departure time {weeks:d} weeks in the future starting current date'))
def set_departure_time(home, weeks: int):
    home.set_departure_time(weeks)

@when('Uncheck the "Check accommodation with booking.com" option')
def uncheck_accommodation(home):
    home.uncheck_accommodation_option()

@when('Click the search button')
def click_search_btn(home):
    home.click_search_btn()

@then('I am redirected to search results page')
def redirected_to_search_results(page: Page):
    expect(page).to_have_url(re.compile(r"/search/results", re.IGNORECASE))