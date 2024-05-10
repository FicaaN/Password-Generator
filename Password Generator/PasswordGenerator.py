import string
import random

def generate_password(length: int, use_lower: bool, use_upper: bool, use_digits: bool, use_special_char: bool) -> str:
    characters = []

    if use_lower:
        characters.extend(string.ascii_lowercase)
    if use_upper:
        characters.extend(string.ascii_uppercase)
    if use_digits:
        characters.extend(string.digits)
    if use_special_char:
        characters.extend(string.punctuation) # All the characters:  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    length = max(length, 6)

    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("Welcome to password generator!")
    print("Minimum length of the password: 6 characters | Maximum length of the password: 50 characters\n")

    # LENGTH
    while True:
        input_length = input("Enter the length of the password: ")

        try:
            length = int(input_length)
            if length <= 0:
                print("Invalid length. Please enter a positive number.")
            elif length < 6:
                print("Minimum length must be 6 characters. Please enter again.")
            elif length > 50:
                print("Maximum length is 50 characters. Please enter again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid length.")

    # LOWERCASE
    while True:
        input_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower()

        if input_lowercase == "yes" or input_lowercase == "no":
            use_lower = input_lowercase == "yes"
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    # UPPERCASE
    while True:
        input_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()

        if input_uppercase == "yes" or input_uppercase == "no":
            use_upper = input_uppercase == "yes"
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    # DIGITS
    while True:
        input_digits = input("Include digits? (yes/no): ").strip().lower()

        if input_digits == "yes" or input_digits == "no":
            use_digits = input_digits == "yes"
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    # SPECIAL CHARACTERS
    while True:
        input_special_char = input("Include special characters? (yes/no): ").strip().lower()

        if input_special_char == "yes" or input_special_char == "no":
            use_special_char = input_special_char == "yes"
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    # CHECKING FOR THE REQUIREMENTS
    if not (use_lower or use_upper or use_digits or use_special_char):
        print("The password cannot be generated.")
        print("At least one type of characters must be selected.")
    else:
        try:
            password = generate_password(length, use_lower, use_upper, use_digits, use_special_char)
            print("Generated Password:", password)
        except ValueError as error:
            print("The password could not be generated. Reason:", error)

if __name__ == "__main__":
    main()