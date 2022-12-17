from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():

    web = web_input.get()
    user = email_input.get()
    pw = password_input.get()
    new_data = {
        web: {
            "email": user,
            "password": pw,
        }
    }

    if web == "" or user == "" or pw == "":
        messagebox.showwarning("Oops", "Please don't leave any fields empty!")

    else:
        try:
            with open('passwords.json', 'r') as data:
                #Read old data
                file = json.load(data)
        except FileNotFoundError:
            with open('passwords.json', 'w') as data:
                #Create file
                json.dump(new_data, data, indent=4)
        else:   
            #Update old data with new data
            file.update(new_data)

            with open('passwords.json', 'w') as data:
                #Save updated data
                json.dump(file, data, indent=4)
        finally:        
            web_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- SEARCH FUNCTION ------------------------------- #
def find_password():
    web = web_input.get()
    try:
        with open('passwords.json', 'r') as data:
            file = json.load(data)
    except FileNotFoundError:
        messagebox.showwarning("Error", "No Data File Found")
    else:
        if web in file:
            messagebox.showinfo(web, f"Website:\n{web}\nEmail:\n{file[web]['email']}\nPassword:\n{file[web]['password']} ")
        else:
            messagebox.showwarning('Not found', f'No details for {web} exists')
# ---------------------------- UI SETUP ------------------------------- #
#Initialize window
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

#Logo position
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()
canvas.grid(row=0, column=1)

#Website input
website = Label(window, text='Website:')
website.grid(row = 1, column = 0)
web_input = Entry(window, width=20)
web_input.focus()
web_input.grid(row=1, column = 1)
web_button = Button(window, text='Search', width = 11, command=find_password)
web_button.grid(row=1, column=2)


#Email/Username input
email = Label(window, text='Email/Username:')
email.grid(row = 2, column = 0)
email_input = Entry(window, width=35)
email_input.insert(0, "test@email.com")
email_input.grid(row=2, column = 1, columnspan=2)

#Password input
password = Label(window, text='Password:')
password.grid(row = 3, column = 0)
password_input = Entry(window, width=20)
password_input.grid(row=3, column = 1)
password_button = Button(window, text='Generate Password', width=11, command=generate_password)
password_button.grid(row = 3, column = 2)

#Add button
add_button = Button(window, text='Add', width=33, command=save_entry)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()