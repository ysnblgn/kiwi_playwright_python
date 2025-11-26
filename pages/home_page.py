import logging
import re
from datetime import date, timedelta
from playwright.sync_api import Page, expect, TimeoutError

from tests.utils.utils import get_airport_name

logger = logging.getLogger(__name__)


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.cookies_accept_btn = page.get_by_role("button", name="Accept")
        self.return_btn = page.get_by_role("button", name="Return")
        self.trip_type_one_way_btn = page.locator('[data-test="ModePopupOption-oneWay"]')
        self.departure_input = page.locator('[data-test="PlacePickerInput-origin"] input')
        self.arrival_input = page.locator('[data-test="PlacePickerInput-destination"] input')
        self.suggestion_rows = page.locator('[data-test="PlacePickerRow-station"]')
        self.departure_chip = page.locator('[data-test="PlacePickerInput-origin"] [data-test="PlacePickerInputPlace"]')
        self.arrival_chip = page.locator(
            '[data-test="PlacePickerInput-destination"] [data-test="PlacePickerInputPlace"]')
        self.date_input = page.locator('[data-test="SearchDateInput"]')
        self.datepicker = page.locator('[data-test="NewDatePickerOpen"]')
        self.set_dates_btn = page.get_by_role("button", name="Set dates")
        self.accommodation_checkbox = page.get_by_role("checkbox",
                                                       name=re.compile("Check accommodation with", re.IGNORECASE))
        self.search_btn = page.locator('[data-test="LandingSearchButton"]')

    def open(self, url: str) -> None:
        self.page.goto(url)

    def accept_cookies(self):
        try:
            self.cookies_accept_btn.click(timeout=5000)
        except TimeoutError:
            logger.error("Cookie banner not found. Continuing the test.")
            pass

    def select_one_way_trip(self) -> None:
        self.return_btn.click(force=True)
        self.trip_type_one_way_btn.click()

    def set_airport(self, code: str, direction: str):
        airport_name = get_airport_name(code)
        code_text = code.upper()

        if direction == "departure":
            input_box = self.departure_input
            chip = self.departure_chip
        elif direction == "arrival":
            input_box = self.arrival_input
            chip = self.arrival_chip
        else:
            raise ValueError("direction must be 'departure' or 'arrival'.")

        input_box.clear()
        input_box.fill('')
        input_box.click()
        input_box.fill(airport_name)

        self.suggestion_rows.first.wait_for(state="visible", timeout=10000)

        pattern = re.compile(re.escape(airport_name), re.UNICODE)

        target_row = self.suggestion_rows.get_by_text(pattern).first
        expect(target_row).to_be_visible(timeout=10000)

        target_row.click()

        expect(chip).to_be_visible()
        expect(chip).to_contain_text(code_text)

    def set_departure_time(self, weeks: int):
        target = date.today() + timedelta(weeks=weeks)
        target_value = target.strftime("%Y-%m-%d")

        self.date_input.click()

        expect(self.datepicker).to_be_visible(timeout=5000)

        day_btn = self.datepicker.locator(f'[data-value="{target_value}"]')
        expect(day_btn).to_be_visible(timeout=5000)

        day_btn.click()

        self.set_dates_btn.click()

    def uncheck_accommodation_option(self):
        self.accommodation_checkbox.uncheck(force=True)
        expect(self.accommodation_checkbox).not_to_be_checked()

    def click_search_btn(self):
        self.search_btn.click()
