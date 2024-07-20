import string
import random

class PasswordGenerator:
    def __init__(self):
        self.characters = []
        self.length = 6
        self.use_lower = False
        self.use_upper = False
        self.use_digits = False
        self.use_special_char = False

    def set_length(self, length: int):
        if length < 6:
            raise ValueError("Minimum length must be 6 characters.")
        if length > 50:
            raise ValueError("Maximum length is 50 characters.")
        self.length = length

    def set_use_lower(self, use: bool):
        self.use_lower = use

    def set_use_upper(self, use: bool):
        self.use_upper = use

    def set_use_digits(self, use: bool):
        self.use_digits = use

    def set_use_special_char(self, use: bool):
        self.use_special_char = use

    def generate_password(self) -> str:
        if not (self.use_lower or self.use_upper or self.use_digits or self.use_special_char):
            raise ValueError("At least one character type must be selected.")
        
        self.characters = []
        if self.use_lower:
            self.characters.extend(string.ascii_lowercase)
        if self.use_upper:
            self.characters.extend(string.ascii_uppercase)
        if self.use_digits:
            self.characters.extend(string.digits)
        if self.use_special_char:
            self.characters.extend(string.punctuation)

        password = ''.join(random.choices(self.characters, k=self.length))
        return password

def run_password_generator():
    print("Welcome to password generator!")
    print("Minimum length of the password: 6 characters | Maximum length of the password: 50 characters\n")
    
    generator = PasswordGenerator()

    # LENGTH
    while True:
        input_length = input("Enter the length of the password: ")
        try:
            length = int(input_length)
            generator.set_length(length)
            break
        except ValueError as e:
            print(e)

    # LOWERCASE
    while True:
        input_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower()
        if input_lowercase in ["yes", "no"]:
            generator.set_use_lower(input_lowercase == "yes")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    # UPPERCASE
    while True:
        input_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
        if input_uppercase in ["yes", "no"]:
            generator.set_use_upper(input_uppercase == "yes")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    # DIGITS
    while True:
        input_digits = input("Include digits? (yes/no): ").strip().lower()
        if input_digits in ["yes", "no"]:
            generator.set_use_digits(input_digits == "yes")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    # SPECIAL CHARACTERS
    while True:
        input_special_char = input("Include special characters? (yes/no): ").strip().lower()
        if input_special_char in ["yes", "no"]:
            generator.set_use_special_char(input_special_char == "yes")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    # CHECKING FOR THE REQUIREMENTS
    try:
        password = generator.generate_password()
        print("Generated Password:", password)
    except ValueError as e:
        print("The password could not be generated. Reason:", e)

if __name__ == "__main__":
    run_password_generator()
