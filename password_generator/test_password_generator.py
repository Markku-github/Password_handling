import unittest
from mock import patch
import string
from password_generator import generate_password
from password.pwd import Password

class TestPwd(unittest.TestCase):

    def setUp(self):
        self.letters_list = string.ascii_letters
        self.digits_list = string.digits
        self.specials_list = string.punctuation
        self.lenght = 10

    def test_generate_password_no_digits_no_special(self):
        gen_pwd = generate_password(10, False, False)
        for char in gen_pwd:
            self.assertIn(char, self.letters_list, msg="Generated password contained a number or special character even though it shouldn't have")

    def test_generate_password_digits_no_special(self):
        gen_pwd = generate_password(10, True, False)
        self.assertTrue(any(char.isalpha() for char in gen_pwd), msg="Generated password not contain any letter even it should have!")
        self.assertTrue(any(char.isdigit() for char in gen_pwd), msg="Generated password not contain any number even it should have!")

    def test_generate_password_no_digits_special(self):
        gen_pwd = generate_password(10, False, True)
        self.assertTrue(any(char.isalpha() for char in gen_pwd), msg="Generated password not contain any letter even it should have!")
        self.assertTrue(any(not char.isalnum() for char in gen_pwd), msg="Generated password not contain any special character even is should have!")

    def test_generate_password_digits_special(self):
        gen_pwd = generate_password(10, True, True)
        self.assertTrue(any(char.isalpha() for char in gen_pwd), msg="Generated password not contain any letter even is should have!")
        self.assertTrue(any(char.isdigit() for char in gen_pwd), msg="Generated password not contain any number even is should have!")
        self.assertTrue(any(not char.isalnum() for char in gen_pwd), msg="Generated password not contain any special character even is should have!")

    def test_generate_password_lenght(self):
        gen_pwd = generate_password(self.lenght, True, True)
        self.assertEqual(self.lenght, len(gen_pwd), msg="Generated password lenght was not what expected!")

    def tearDown(self):
        del self.letters_list
        del self.digits_list
        del self.specials_list
        del self.lenght

if __name__ == '__main__':
    unittest.main()