import json
from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    liste = []
    for i in range(1, 17):
        if i < 9:
            liste.append(random.choice(letters))
        elif i < 13:
            liste.append(random.choice(numbers))
        else:
            liste.append(random.choice(symbols))
    random.shuffle(liste)
    passwordd = "".join(liste)
    password_entry.delete(0, END)
    password_entry.insert(END, passwordd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_ = website_entry.get()
    password_ = password_entry.get()
    email = user_entry.get()
    if email == "" or password_ == "" or website_ == "":
        messagebox.showerror(title="Error", message="Please, enter the information completely.")
    else:
        ok = messagebox.askokcancel(title="", message=f"Your information will be saved as follows:\n\n"
                                                      f"Website:{website_}\n Email:{email}\n Password:{password_}")
        if ok:
            new_data = {website_: {"email": email, "password": password_}}
            file = open("data.json", 'r')
            data = json.load(file)
            data.update(new_data)


def search():
    website_ = website_entry.get()
    file = open("data.json")
    data = json.load(file)
    if website_ in data:
        messagebox.showinfo(title=website_, message=f"Email/Username:{data[website_]['email']}\n Password:{data[website_]['password']}")
    else:
        messagebox.showinfo(title=website_, message=f"No details for {website_} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=450, height=400)
window.config(padx=50, pady=50)
window.title("My Pass")

canvas = Canvas(width=200, height=224, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website = Label(text="Website", font=("Arial", 8, "bold"))
website.grid(row=1, column=0)

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()

user_name = Label(text="Email/Username", font=("Arial", 8, "bold"))
user_name.grid(row=2, column=0, )

user_entry = Entry(width=51)
user_entry.grid(row=2, column=1, columnspan=2)

password = Label(text="Password", font=("Arial", 8, "bold"))
password.grid(row=3, column=0)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
