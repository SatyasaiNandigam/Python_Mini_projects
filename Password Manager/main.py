from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    specials = ['!', '@', '#', '%', '$', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_specials = [choice(specials) for _ in range(randint(2, 4))]
    password_list = password_specials + password_letters + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    Password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website_data = Website_name.get()
    email_data = Email_or_username_input.get()
    password_data = Password_input.get()
    new_data = {
        website_data.title(): {
            "email": email_data,
            "password": password_data
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title='Empty field', message="HEy , don't leave fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading the data from the json file
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # writing the data to the json file
                json.dump(new_data, data_file, indent=4)
        else:
            # updating the data of the json file
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # writing the data to the json file
                json.dump(data, data_file, indent=4)
        finally:
            Website_name.delete(0, END)
            Password_input.delete(0, END)

# -----------------------------SEARCH WEBSITE-------------------------#


def search_website():
    website = Website_name.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\npassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details about {website} website!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

Website_label = Label(text="\tWebsite:")
Website_label.grid(column=0, row=1)

Email_or_username_label = Label(text="Email/Username:")
Email_or_username_label.grid(column=0, row=2)

Password_label = Label(text="\tPassword:")
Password_label.grid(column=0, row=3)

Website_name = Entry(width=42)
Website_name.grid(column=1, row=1)
Website_name.focus()

search_button = Button(width=15, text="Search", highlightthickness=0, command=search_website)
search_button.grid(column=2, row=1)


Email_or_username_input = Entry(width=60)
Email_or_username_input.grid(column=1, row=2, columnspan=2)
Email_or_username_input.insert(0, "satyasai9441@gmail.com")

Password_input = Entry(width=42, highlightthickness=0)
Password_input.grid(column=1, row=3)

Generate_password_button = Button(text="Generate Password", highlightthickness=0, command=create_password)
Generate_password_button.grid(column=2, row=3)

Add_button = Button(text="Add", width=51, command=save_data)
Add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
