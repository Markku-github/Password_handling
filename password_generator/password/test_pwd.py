import unittest
from mock import patch
from pwd import Password
import string

class TestPwd(unittest.TestCase):

    def setUp(self):
        self.pwd = Password(10, True, True)
        self.test_letters = string.ascii_letters
        self.test_digits_list = string.digits
        self.test_specials_list = string.punctuation
        self.test_lenght = 10
        self.test_password = "password"

    def test_letters(self):
        self.pwd.letters = self.test_letters
        self.assertEqual(self.test_letters, self.pwd.letters, msg="Setter or getter of letters is not work correctly!")

    def test_digits_list(self):
        self.pwd.digits_list = self.test_digits_list
        self.assertEqual(self.test_digits_list, self.pwd.digits_list, msg="Setter or getter of digits list is not work correctly!")

    def test_specials_list(self):
        self.pwd.specials_list = self.test_specials_list
        self.assertEqual(self.test_specials_list, self.pwd.specials_list, msg="Setter or getter of special characters list is not work correctly!")

    def test_lenght(self):
        self.pwd.lenght = self.test_lenght
        self.assertEqual(self.test_lenght, self.pwd.lenght, msg="Setter or getter of password lenght is not work correctly!")

    @patch.object(Password, "_Password__init_digits_list")
    def test_has_digit_true(self, mock_init_digits_list):
        self.pwd.has_digit = True
        mock_init_digits_list.assert_called_once_with(True)

    @patch.object(Password, "_Password__init_digits_list")
    def test_has_digit_false(self, mock_init_digits_list):
        self.pwd.has_digit = False
        mock_init_digits_list.assert_called_once_with(False)

    @patch.object(Password, "_Password__init_specials_list")
    def test_has_special_true(self, mock_init_specials_list):
        self.pwd.has_special = True
        mock_init_specials_list.assert_called_once_with(True)

    @patch.object(Password, "_Password__init_specials_list")
    def test_has_special_false(self, mock_init_specials_list):
        self.pwd.has_special = False
        mock_init_specials_list.assert_called_once_with(False)

    def test_password(self):
        self.pwd.password = self.test_password
        self.assertEqual(self.test_password, self.pwd.password, msg="Setter or getter of password is not work correctly!")

    def test_init_digits_list(self):
        self.pwd.__init_digits_list = True
        test_digits_list = string.digits
        self.assertEqual(test_digits_list, self.pwd.digits_list, msg="Setter or getter of digits list initializion is not work correctly!")

    def test_init_specials_list(self):
        self.pwd.__init_specials_list = True
        test_specials_list = string.punctuation
        self.assertEqual(test_specials_list, self.pwd.specials_list, msg="Setter or getter of special characters list initialization is not work correctly!")

    def tearDown(self):
        del self.pwd
        del self.test_letters
        del self.test_digits_list
        del self.test_specials_list
        del self.test_lenght
        del self.test_password

if __name__ == '__main__':
    unittest.main()