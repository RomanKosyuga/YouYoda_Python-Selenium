import unittest
from selenium import webdriver

from pages import events_page as ep
from pages import base_page


class Events(unittest.TestCase):
    """Docstring for Events."""
    DRIVER = webdriver.Chrome()

    def setUp(self):
        self.driver = Events.DRIVER
        self.events_page = ep.EventsPage(self.driver)
        self.events_page.go_to()

    @classmethod
    def tearDownClass(cls):
        cls.DRIVER.quit()

    def test_events_header(self):
        self.assertEqual("Events", self.events_page.check_page_header().text)

    def test_events_button(self):
        self.driver.get(base_page.ABOUT_PAGE_URL)
        self.assertTrue(self.events_page.click_on_event_button())

    def test_navigation_buttons(self):
        self.assertTrue(self.events_page.click_on_next_button())
        self.assertTrue(self.events_page.click_on_prev_button())


if __name__ == "__main__":
    unittest.main(verbosity=2)
