import string # Import all type of characters, numbers, digits, special characters, etc.

class Password:
    def __init__(self, lenght, has_digit, has_special, password = ""):
        self.lenght = lenght # The password exact lenght.
        self.letters = string.ascii_letters # List of all english letters. Other languages letters might be implemented later.
        self.has_digit = has_digit # Boolean to know whether the password should contain number or not.
        self.has_special = has_special # Boolean to know whether the password should contain special character or not.
        self.password = password # Variable which contain the password.

    @property
    def letters(self): # Get method for list of letters used for the password.
        return self._letters

    @letters.setter
    def letters(self, letters):
        self._letters = letters

    @property
    def digits_list(self): # Get method for list of numbers used for the password.
        if hasattr(self,'_digits_list'):
            return self._digits_list
        else:
            pass

    @digits_list.setter
    def digits_list(self, digits_list):
        self._digits_list = digits_list

    @property
    def specials_list(self): # Get method for list of special characters used for the password.
        if hasattr(self, '_specials_list'):
            return self._specials_list
        else:
            pass

    @specials_list.setter
    def specials_list(self, specials_list):
        self._specials_list = specials_list

    @property
    def lenght(self): # Get method for the password lenght.
        return self._lenght

    @lenght.setter
    def lenght(self, lenght): # Set method for the password lenght.
        self._lenght = lenght

    @property
    def has_digit(self): # Get method to know whether the password should contain a number or not.
        return self._has_digit

    @has_digit.setter
    def has_digit(self, has_digit): # Set method to determine whether the password should contain a number or not.
        self._has_digit = has_digit
        self.__init_digits_list(self._has_digit) # Call private function to initialize list of numbers if needed.

    @property
    def has_special(self): # Get method to know whether the password should contain a special character or not.
        return self._has_special

    @has_special.setter
    def has_special(self, has_special): # Set method to determine whether the password should contain a special character or not.
        self._has_special = has_special
        self.__init_specials_list(self._has_special) # Call private function to initialize list of special characters if needed.
        # Later, the possibility of providing a custom list as argument could be added to this.

    @property
    def password(self): # Get method for the password
        return self._password

    @password.setter
    def password(self, password): # Set method for the password
        self._password = password

    def __init_digits_list(self, has_digit): # Private function which initialize list of numbers used for the password if needed.
        self.digits_list = []
        if has_digit:
            self._digits_list = string.digits # List of numbers used for the password.
        else:
            del self._digits_list # Delete list of numbers if not needed.

    def __init_specials_list(self, has_special): # Private function which initialize list of special characters used for the password if needed.
        self.specials_list = []
        if has_special:
            self._specials_list = special = string.punctuation # List of special characters used for the password.
        else:
            del self._specials_list # Delete list of special characters if not needed.