""" test case to show your favourite courses as a trainer """

import unittest
from selenium import webdriver
from pages import login_page as lp
from pages import profile_page as pp

class FavouriteTrainer(unittest.TestCase):
    """ login as a trainer and check your favourite courses """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = lp.LoginPage(self.driver)
        self.profile_page = pp.ProfilePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_fav_list(self):
        """ checks your favourite courses by clicking 'Show all' button"""
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        self.profile_page.click_on_show_fav_courses()
        self.profile_page.click_on_show_fav_courses()

if __name__ == '__main__':
    unittest.main()
