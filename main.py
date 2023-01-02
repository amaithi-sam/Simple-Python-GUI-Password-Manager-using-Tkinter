import random
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

#----------------------PASSWORD GENERATOR--------------


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def gen_password():

    password_letters = [choice(letters) for item in range(randint(8, 10))]
    password_symbols = [choice(symbols) for item in range(randint(2, 4))]
    password_num = [choice(numbers) for item in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_num

    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)



#----------------------SAVE PASSWORD-------------------
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) ==0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Alert", message="one of the fields are left empty..!")

    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the Details Entered: \n\n Email : \t   {email}\n Password :  {password}\n\n Is it ok to Save..?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                file.close()
                web_entry.delete(0, 'end')
                email_entry.delete(0, 'end')
                pass_entry.delete(0, 'end')

#-----------------------UI SETUP-----------------------
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=logo_image)
canvas.grid(column=1, row=0)
window.config(padx=20, pady=20)

#website_label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

#Email/USername_label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, pady=4)

#Password_label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, pady=4)

# Entry - Website
web_entry = Entry(width=53)
web_entry.grid(column=1, row=1, columnspan=2, sticky='w', pady=4)
web_entry.focus()

# Entry - Email
email_entry = Entry(width=53)
email_entry.grid(column=1, row=2, columnspan=2, sticky='w', pady=4)
email_entry.insert(0, "@gmail.com")

# Entry - Password
pass_entry = Entry(width=10)
pass_entry.grid(column=1, row=3, sticky='NSEW', pady=4)

# Button - Generate Password
gen_button = Button(text="Generate Password", width=15, command=gen_password)
gen_button.grid(column=2, row=3, sticky='w', pady=4)

# Button - Add
add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='NSEW', pady=4)


window.mainloop()
































