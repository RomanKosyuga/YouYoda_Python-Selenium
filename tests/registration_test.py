import unittest
from selenium import webdriver
from pages import base_page
from pages import temporary_email_page as tep
from pages import registration_page as reg_p
from pages import login_page as lp
from pages import home_page as hp


class UsersSignUP(unittest.TestCase):
    """Test sign-up possibility into system"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(base_page.BASE_URL)
        self.main_window = self.driver.window_handles[0]
        self.driver.execute_script('window.open("{}");'.format(tep.TEMPORARY_EMAIL_CLIENT))
        self.email_window = self.driver.window_handles[1]
        self.sign_up_window = reg_p.RegistationPage(self.driver)
        self.email_service = tep.TemporaryEmailPage(self.driver)
        self.login_window = lp.LoginPage(self.driver)
        self.home_page = hp.HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def get_temporary_email(self):
        """method to test possibility getting temporary email"""
        self.driver.switch_to.window(self.email_window)
        self.email_service.get_temporary_email()

    def sign_up_as_user(self):
        """method to test possibility registration"""
        self.driver.switch_to.window(self.main_window)
        self.sign_up_window.open_sign_up_window()
        self.sign_up_window.fill_in_email_field()
        self.sign_up_window.fill_in_password_fields()
        self.sign_up_window.confirm_sign_up()

    def sign_up_as_teacher(self):
        """method to test possibility registration"""
        self.driver.switch_to.window(self.main_window)
        self.sign_up_window.open_sign_up_window()
        self.sign_up_window.mark_as_teacher()
        self.sign_up_window.fill_in_email_field()
        self.sign_up_window.fill_in_password_fields()
        self.sign_up_window.confirm_sign_up()

    def confirm_activation(self):
        """method to test possibility confirming activation account"""
        self.driver.switch_to.window(self.email_window)
        self.email_service.open_email()
        self.email_service.activate_account()

    def sign_in(self):
        """method to test sign-in with created account"""
        data_for_sing_in = self.sign_up_window.create_dictionary_for_login()
        self.login_window.sign_in_as(**data_for_sing_in)

    def check_if_teacher_functions_have_applied(self):
        """method to test if teacher functions applied to the account """
        self.sign_up_window.check_if_own_courses_have_applied()

    def test_registration_as_user(self):
        """test sign-up possibility as the user """
        self.get_temporary_email()
        self.sign_up_as_user()
        self.confirm_activation()
        self.sign_in()

    def test_registration_as_teacher(self):
        """test sign-up possibility as the teacher """
        self.get_temporary_email()
        self.sign_up_as_teacher()
        self.confirm_activation()
        self.sign_in()
        self.check_if_teacher_functions_have_applied()


if __name__ == "__main__":
    unittest.main(verbosity=2)
