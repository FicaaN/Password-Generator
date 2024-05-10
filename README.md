# 🔐**Password Generator**

Welcome to my first Python project - a password generator program! This project includes both a **terminal-based version** (**PasswordGenerator**) and a **GUI-based application** (**PasswordGeneratorApp**) for generating secure passwords. The GUI version utilizes **customTkinter** for its interface.

## 📁**Files Included**
* **PasswordGenerator.py** - Terminal-based password generator
* **PasswordGeneratorApp.py** - GUI-based password generator application
* **password_generator_icon.ico** - Icon file for the GUI application

## 🚀**How to Run**
To use this program, make sure that you have **Python** installed. For the GUI-based application, you'll also need to install **customTkinter** library. You can install it with **terminal** or **command prompt**, with the following command:
```bash
pip install customtkinter
```
To run the program, use the following command:
```bash
python PasswordGeneratorApp.py
```

## 📝**Specifications**
* **Password Length** - The user can set the password length within the range of **6** to **50** characters. 
* **Character Types** - The user must select at least one of the following character types:
  
  * **Lowercase Letters** - Includes lowercase alphabetic characters (**a-z**).
  * **Uppercase Letters** - Includes uppercase alphabetic characters (**A-Z**).
  * **Digits** - Includes numeric characters (**0-9**).
  * **Special Characters** - Includes special characters: **!"#$%&'()*+,-./:;<=>?@[]^_`{|}~**

## ⚠️**Notes**
* The application ensures that at least one character type is selected before generating the password.
* If no character type is selected or invalid password length is provided, the password will not be generated.

## 🖥️**Icon Usage**
If you wish to use the provided icon for application, or any other, follow these steps:
* Place the icon file in the same project folder as the PasswordGeneratorApp.
* Navigate to line 66 in the script and remove the comment # at the beginning.
* If you are using your own icon, put the icon file name like this:
```python
app.iconbitmap("your-icon-filename.ico")
```

## 🖼️**Examples**
* **Terminal-based version**
  
![Screenshot_1](https://github.com/FicaaN/Password-Generator/assets/152323594/918919c7-6d08-49c1-9421-027a1c629ed8)

* **GUI-based application**

![Screenshot 2024-05-10 233016](https://github.com/FicaaN/Password-Generator/assets/152323594/6b4233f4-4087-42f4-8977-37a4425dd501)
