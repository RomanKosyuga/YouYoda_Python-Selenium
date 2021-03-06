"""Class for the Events page with methods which are used for testing"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages import base_page
from pages.base_page import BasePage
from locators.events_locators import EventsPageLocators as epl
from selenium.common.exceptions import TimeoutException
from helpers import login_helpers

class EventsPage(BasePage):
    """docstring for EventsPage."""

    def go_to(self):
        """Method for redirecting to events page"""
        self.driver.get(base_page.EVENTS_PAGE_URL)

    def check_page_header(self):
        return self.driver.find_element_by_class_name(epl.HEADER_TEXT_CLASS_NAME)

    def click_on_event(self):
        return self.wait.until(EC.element_to_be_clickable(epl.EVENT_HEADER)).click()

    def click_on_event_button(self):
        try:
            self.click_on_element_by_css(epl.EVENT_BUTTON_IN_HEADER)
            return True
        except Exception as ex:
            raise ex

    def click_on_next_button(self):
        try:
            self.click_on_element_by_css(epl.NAVI_NEXT_BUTTON)
            return True
        except Exception as ex:
            raise ex

    def click_on_prev_button(self):
        try:
            self.click_on_element_by_css(epl.NAVI_PREV_BUTTON)
            return True
        except Exception as ex:
            raise ex

    def is_search_button_presented(self):
        """ Check Search button present """
        try:
            self.find_element_by_css(epl.EVENT_SEARCH_BUTTON)
            return True
        except TimeoutException:
            return False

    def click_on_search_button(self):
        """Method to check if button clickable"""
        self.click_on_element_by_css(epl.EVENT_SEARCH_BUTTON)

    def click_on_search_submit(self):
        """Method to click on search submit"""
        self.click_on_element_by_css(epl.EVENT_SEARCH_SUBMIT)

    def clear_search_field(self):
        self.clear_text_field_by_css(epl.EVENT_SEARCH_BUTTON)

    def fill_in_search_field_by_css(self):
        """Method for filling in the text field with text"""
        self.fill_in_text_field_by_css(epl.EVENT_SEARCH_BUTTON, "Fly")

    def check_placeholder_text(self):
        # return self.wait.until(EC.visibility_of_element_located(by_css))
        actual_placeholder_text = self.find_element_by_css(epl.EVENT_SEARCH_BUTTON).get_attribute("placeholder")
        return actual_placeholder_text

    def is_header_presented(self, by_css):
        """ Check header present after search """
        try:
            self.find_element_by_css(by_css)
            return True
        except TimeoutException:
            return False

    def search_event(self, text):
        self.click_on_element_by_css(epl.SEARCH)
        self.fill_in_text_field_by_css(epl.SEARCH, text)

    def is_no_events_message_on_page(self):
        try:
            self.find_element_by_css(epl.NO_EVENTS_MESSAGE)
            return True
        except TimeoutException:
            return False

    def write_a_comment(self, comment=None):
        """Method for writing a comment under event"""
        if not comment:
            comment = login_helpers.get_random_pass(16)
        self.fill_in_text_field_by_css(epl.COMMENT_FIELD, comment)
        return comment

    def leave_comment(self):
        """Method for leaving a comment under event"""
        self.click_on_element_by_css(epl.LEAVE_COMMENT_BUTTON)

    def find_comment(self):
        """Method used to find first comment on event details page"""
        return self.find_element_by_css(epl.FIRST_COMMENT_TEXT)

    def is_comment_textarea_present(self):
        """Method for check if text area for comment is present"""
        try:
            self.find_element_by_css(epl.COMMENT_FIELD)
            return True
        except TimeoutException:
            return False

    def go_to_who_play_with_me(self):
        self.click_on_element_by_css(epl.WHO_PLAY_WITH_ME)

    def go_to_first_event(self):
        self.click_on_element_by_css(epl.FIRST_EVENT_CARD)


    def is_details_comment_list_present(self):
        """Method for check if text area for comment is present"""
        try:
            self.find_element_by_css(epl.EVENT_DETAILS_COMMENT_LIST)
            return True
        except TimeoutException:
            return False
