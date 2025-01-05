import random # Import for random number generators.
from password.pwd import Password

def generate_password(lenght, digits=True, special_char=True):
    pwd = Password(lenght, digits, special_char)

    letters_list = pwd.letters # Get list of letters used for the password. This will be used later separately from the character list.
    characters = letters_list # Add list of letters used for the password to the list of characters.
    if digits: # If digits is true, in other word, if the password should contain a number.
        digits_list = pwd.digits_list # List of numbers used to generate the password.
        characters += digits_list # Numbers are added to the list of characters.

    if special_char: # If special_char is true, in other word, if the password should contain a special character.
        specials_list = pwd.specials_list # List of special characters used to generate the password.
        characters += specials_list # Special characters (string.punctuation) will be added to the list of characters.

    meets_criteria = False # Boolean used to check whether the password criteria are met.
    has_letter = False # Used for check if the password has letter.
    has_number = False # Used for check if the password has number.
    has_special = False # Used for check if the password has special character.

    gen_pwd = "" # Variable where the password will be generated.

    while not meets_criteria or not len(gen_pwd) == lenght: # Loop until criteria met and password lenght is correct.
        new_char = random.choice(characters) # Pick random character from characters list.
        gen_pwd += new_char # Add new character to the password.

        if new_char in letters_list: # Check if new character is letter. 
            # It is for case where the password should contain a number, a special character or both. In that case we should be sure that there is still at least one letter.
            has_letter = True

        if digits and new_char in digits_list: # Check if the password should contain a number and then if new character is number.
            has_number = True

        if special_char and new_char in specials_list: # Check if the password should contain a special character and then if new character is special character.
            has_special = True

        meets_criteria = True # Set meets_criteria to true for case where the password expected contain only letters.
        if digits: # If the password should contain numbers.
            meets_criteria = has_letter and has_number # If number exist in the password (if has_humber was set to true above) criteria met.
        if special_char: # If the password should contain special characters.
            meets_criteria = meets_criteria and has_letter and has_special # If special character exist in the password (if has_special was set to true above) criteria met.
            # This check also if both number and special character was required.

        if len(gen_pwd) > lenght: # If the generated password become longer than exact lenght, then remove first character from the password.
            gen_pwd = gen_pwd[1:]

    return gen_pwd 

#gen_pwd = generate_password(10)
#print(gen_pwd)