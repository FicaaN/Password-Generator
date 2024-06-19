import customtkinter
import string
import random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

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

    if int(length) >= 6 and int(length) <= 50:
        password = ''.join(random.choices(characters, k=int(length)))
        return password
    else:
        password = ""
        return password

def generate_and_update_password():
    length = length_entry.get()

    # If user doesn't enter any length or if the length is not an integer, return
    if not length or not length.isdigit():
        clear_password()
        return

    if int(length) < 6 and int(length) > 50:
        clear_password()
        return
            
    use_lower = lower_checkbox.get()
    use_upper = upper_checkbox.get()
    use_digits = digits_checkbox.get()
    use_special_char = special_checkbox.get()

    # If user doesn't check any checkbox, return
    if not any([use_lower, use_upper, use_digits, use_special_char]):
        clear_password()
        return

    password = generate_password(length, use_lower, use_upper, use_digits, use_special_char)

    button_entry.configure(state="normal")
    button_entry.delete(0, "end")
    button_entry.insert(0, password)
    button_entry.configure(state="readonly")

def clear_password():
    button_entry.configure(state="normal")
    button_entry.delete(0, "end")
    button_entry.insert(0, "")
    button_entry.configure(state="readonly")

app = customtkinter.CTk()
app.title("Password Generator")
#app.iconbitmap("password_generator_icon.ico")
app.minsize(550, 300)
app.maxsize(550, 300)
app.grid_columnconfigure(0, weight=1)

text = customtkinter.CTkLabel(app, text="Password Length | Min: 6 - Max: 50", font=("Roboto", 14))
text.grid(row=0, column=0, columnspan=2, pady=(20, 3), sticky="nsew")

length_entry = customtkinter.CTkEntry(app, placeholder_text="Enter the length", justify="center")
length_entry.grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky="ns")

lower_checkbox = customtkinter.CTkCheckBox(app, text="Include Lowercase")
lower_checkbox.grid(row=2, column=0, pady=(20, 10), padx=(55, 0), sticky="w")

upper_checkbox = customtkinter.CTkCheckBox(app, text="Include Uppercase")
upper_checkbox.grid(row=3, column=0, pady=(10, 10), padx=(55, 0), sticky="w")

digits_checkbox = customtkinter.CTkCheckBox(app, text="Include Digits")
digits_checkbox.grid(row=2, column=1, pady=(20, 10), padx=(0, 55), sticky="w")

special_checkbox = customtkinter.CTkCheckBox(app, text="Include Special Characters")
special_checkbox.grid(row=3, column=1, pady=(10, 10), padx=(0, 55), sticky="w")

button = customtkinter.CTkButton(app, text="Generate Password", command=generate_and_update_password)
button.grid(row=4, column=0, columnspan=2, pady=(10, 5), sticky="ns")

button_entry = customtkinter.CTkEntry(app, width=475, justify="center", state="readonly")
button_entry.grid(row=5, column=0, columnspan=2, pady=(5, 20), sticky="ns")

app.mainloop()