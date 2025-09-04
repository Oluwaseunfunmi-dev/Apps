from tkinter import *
from tkinter import messagebox
#import pyperclip(copy and pastes)
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)
password_ = ""
def password_generate():
    global password_

    password_letters= [random.choice(letters) for char in range(nr_letters)]
    password_number= [random.choice(numbers) for char in range(nr_numbers)]
    password_symbols= [random.choice(symbols) for char in range(nr_symbols)]
    password_list = password_symbols + password_number + password_letters
    random.shuffle(password_list)
    password_ ="".join(password_list)
    password.insert(0, f"{password_}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website_response = website.get()
    email_response = email.get()
    password_response = password.get()
    new_data = {
        website_response: {
            "email": email_response,
            "password":password_response,
        }
    }
    if len(website.get())==0 or len(password.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any of the fields empty")

    else:
        try:
            with open("data.json", mode= "r")as data_file:
               #Reading old data
                data = json.load(data_file)
                #Updating old data with new data
                data.update(new_data)
            website.delete(0, END)
            password.delete(0, END)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                #Saving updated data
                json.dump(new_data, data_file, indent=4)
                website.delete(0, END)
                password.delete(0,END)
        else:
            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
                website.delete(0, END)
                password.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_response = website.get()
    try:
        with open("data.json") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message= "No Data File Found.")
    else:
        if website_response in data:
            email_response = data[website_response]["email"]
            password_response = data[website_response]["password"]
            messagebox.showinfo(title=website_response, message=f"Email: {email_response}\nPassword: {password_response}")
        else:
            messagebox.showinfo(title= "Error", message= f"No details for {website_response} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=440, height=440)
window.title("Password Manager")
window.config(padx=50,pady=20)


canvas = Canvas(width= 200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= logo_img)
canvas.grid(column=0,row=0,padx=22, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website = Entry(width=40)
website.focus()
website.grid(column=1, row=1, columnspan=2)

search = Button(text="Search", width=15, command=find_password)
search.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email = Entry(width=40)
email.insert(0,"oluwafikunmioyelade@gmail.com")
email.grid(column=1, row=2,columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)


# Align password entry field to the left
password = Entry(width=21)
password.grid(column=1, row=3)

# Place the "Generate Password" button without extra space between them
generate_password = Button(text="Generate Password", width=15, command=password_generate)
generate_password.grid(column=2, row=3, columnspan=2)

'''def add_password():
    with open("data.txt", mode= "a")as save:
        save.write(f"{website.get()} | {email.get()} | {password.get()}\n")'''

add = Button(text="Add", width=34, command= add_password)
add.grid(column=1, row=4, columnspan=2)



window.mainloop()