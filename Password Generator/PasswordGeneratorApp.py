import customtkinter
import string
import random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class PasswordGeneratorGUI:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.title("Password Generator")
        #self.app.iconbitmap("password_generator_icon.ico")
        self.app.minsize(550, 300)
        self.app.maxsize(550, 300)
        self.app.grid_columnconfigure(0, weight=1)
        
        self.setup_ui()

    def setup_ui(self):
        text = customtkinter.CTkLabel(self.app, text="Password Length | Min: 6 - Max: 50", font=("Roboto", 14))
        text.grid(row=0, column=0, columnspan=2, pady=(20, 3), sticky="nsew")

        self.length_entry = customtkinter.CTkEntry(self.app, placeholder_text="Enter the length", justify="center")
        self.length_entry.grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky="ns")

        self.lower_checkbox = customtkinter.CTkCheckBox(self.app, text="Include Lowercase")
        self.lower_checkbox.grid(row=2, column=0, pady=(20, 10), padx=(55, 0), sticky="w")

        self.upper_checkbox = customtkinter.CTkCheckBox(self.app, text="Include Uppercase")
        self.upper_checkbox.grid(row=3, column=0, pady=(10, 10), padx=(55, 0), sticky="w")

        self.digits_checkbox = customtkinter.CTkCheckBox(self.app, text="Include Digits")
        self.digits_checkbox.grid(row=2, column=1, pady=(20, 10), padx=(0, 55), sticky="w")

        self.special_checkbox = customtkinter.CTkCheckBox(self.app, text="Include Special Characters")
        self.special_checkbox.grid(row=3, column=1, pady=(10, 10), padx=(0, 55), sticky="w")

        button = customtkinter.CTkButton(self.app, text="Generate Password", command=self.generate_and_update_password)
        button.grid(row=4, column=0, columnspan=2, pady=(10, 5), sticky="ns")

        self.button_entry = customtkinter.CTkEntry(self.app, width=475, justify="center", state="readonly")
        self.button_entry.grid(row=5, column=0, columnspan=2, pady=(5, 20), sticky="ns")

    def generate_password(self, length: int, use_lower: bool, use_upper: bool, use_digits: bool, use_special_char: bool) -> str:
        characters = []

        if use_lower:
            characters.extend(string.ascii_lowercase)
        if use_upper:
            characters.extend(string.ascii_uppercase)
        if use_digits:
            characters.extend(string.digits)
        if use_special_char:
            characters.extend(string.punctuation)

        if 6 <= int(length) <= 50:
            password = ''.join(random.choices(characters, k=int(length)))
            return password
        else:
            return ""

    def generate_and_update_password(self):
        length = self.length_entry.get()

        if not length or not length.isdigit():
            self.clear_password()
            return

        if not (6 <= int(length) <= 50):
            self.clear_password()
            return
                
        use_lower = self.lower_checkbox.get()
        use_upper = self.upper_checkbox.get()
        use_digits = self.digits_checkbox.get()
        use_special_char = self.special_checkbox.get()

        if not any([use_lower, use_upper, use_digits, use_special_char]):
            self.clear_password()
            return

        password = self.generate_password(length, use_lower, use_upper, use_digits, use_special_char)

        self.button_entry.configure(state="normal")
        self.button_entry.delete(0, "end")
        self.button_entry.insert(0, password)
        self.button_entry.configure(state="readonly")

    def clear_password(self):
        self.button_entry.configure(state="normal")
        self.button_entry.delete(0, "end")
        self.button_entry.insert(0, "")
        self.button_entry.configure(state="readonly")

    def run(self):
        self.app.mainloop()

def run_password_generator_gui():
    gui = PasswordGeneratorGUI()
    gui.run()

if __name__ == "__main__":
    run_password_generator_gui()
