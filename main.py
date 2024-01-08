from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_1=("Times News Roman",12,"normal")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_random_pass():
    password_entry.delete(0,END)
    password_letter=[random.choice(letters) for num in range(nr_letters)]
    password_symbols=[random.choice(symbols) for num in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for num in range(nr_numbers)]
    password_list=password_letter+password_symbols+password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SEARCH THROUGH FILE------------------------------- #
def search():
    try:
        with open("saved_data.json","r") as file:
            data=json.load(file)
            messagebox.showinfo(title=website_entry.get(),message=f"email: {data[website_entry.get()]['email']}\npassword: {data[website_entry.get()]['password']}")
    except KeyError:
        messagebox.showinfo(title="KeyError", message="The website is not currently exist.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_dict={
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Error", message="Please make sure you do not left any fields empty")
    else:
        try:
            file = open("saved_data.json", "r")
            # Reading new data
            data = json.load(file)
        except JSONDecodeError:
            with open("saved_data.json","w") as file:
                # saving into .json file
                json.dump(new_dict, file, indent=4)
        else:
            #Updating the old data with including new data
            data.update(new_dict)

            file.close()
            with open("saved_data.json","w") as file:
                # saving into .json file
                json.dump(data, file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.minsize(240,200)
window.config(padx=50,pady=50)


canvas=Canvas(width=200,height=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0, column=1)

#Labels
website=Label(text="Website:",font=FONT_1)
website.grid(row=1,column=0)
email=Label(text="Email/Username:",font=FONT_1)
email.grid(row=2,column=0)
password=Label(text="Password:", font=FONT_1)
password.grid(row=3,column=0)
#Entries
website_entry=Entry(width=21)
website_entry.grid(row=1,column=1)

email_entry=Entry(width=35)
email_entry.insert(0,"email@gmail.com")
email_entry.grid(row=2,column=1, columnspan=2)

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

#Buttons
generate_pass=Button(text="Generate Password", font=FONT_1, width=11,command=generate_random_pass)
generate_pass.grid(row=3,column=2)

add_button=Button(text="Add",width=36,font=FONT_1,command=save_data)
add_button.grid(row=4,column=1,columnspan=2)

search_button=Button(text="search", font=FONT_1, width=11,command=search)
search_button.grid(row=1,column=2)

window.mainloop()