from tkinter import *
import tkinter.messagebox
import random
import pyperclip
import json

root = Tk()
root.title("Password Generator")
root.iconbitmap("pass_ico.ico")
root.resizable(0, 0)
root.config(padx=50, pady=50, bg="#9D8189")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

letter_list = [random.choice(letters) for _ in range(nr_letters)]
symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
number_list = [random.choice(numbers) for _ in range(nr_numbers)]

fix_password = letter_list + symbol_list + number_list

random.shuffle(fix_password)

password = "".join(fix_password)


def save():
    def finished():
        entry_web.delete(0, END)
        entry_pass.delete(0, END)
        entry_email.delete(0, END)
        tkinter.messagebox.showinfo("Pop-Up", "Your data has been saved!")

    file_name = "User Data"
    web_data = entry_web.get()
    email_data = entry_email.get()
    pass_data = entry_pass.get()
    new_data = {
        web_data: {
            "Email": email_data,
            "Password": pass_data
        }
    }

    if len(web_data) == 0 or len(email_data) == 0 or len(pass_data) == 0 or web_data == "Enter the Website Name" or \
            email_data == "Enter Your Email/Username" or pass_data == "Enter Your Password":
        tkinter.messagebox.showerror("Error", "Do not leave any field empty!")
    else:
        try:
            with open('user_data.json', 'r') as file_object:
                data = json.load(file_object)
        except FileNotFoundError:
            with open('user_data.json', 'w') as file_object:
                # Save updated data
                json.dump(new_data, file_object, indent=4)
        else:
            data.update(new_data)

            with open('user_data.json', 'w') as file_object:
                # Save updated data
                json.dump(data, file_object, indent=4)
        finally:
            finished()


def generate():
    entry_pass.insert(0, password)
    pyperclip.copy(entry_pass.get())
    tkinter.messagebox.showinfo("Copy to Clipboard", "Password copied to clipboard successfully!")


def search():
    try:
        with open('user_data.json', 'r') as file_object:
            data = json.load(file_object)
            web_data = entry_web.get()
    except FileNotFoundError:
        tkinter.messagebox.showinfo("Error", "No data file found")
    else:
        if web_data in data.keys():
            tkinter.messagebox.showinfo(f"{web_data}", f"Email: {data[web_data]['Email']}\n"
                                                       f"Password: {data[web_data]['Password']}")
        else:
            tkinter.messagebox.showwarning("Data not found!", "No details for the website exists")


pack_frame = Frame(root, bg="#9D8189")
grid_frame = Frame(root, bg="#9D8189")
output_frame = Frame(root, bg="#9D8189")

pack_frame.pack(fill=BOTH, expand=False)
grid_frame.pack(fill=BOTH, expand=False)
output_frame.pack(fill=BOTH, expand=True)

pass_image = PhotoImage(file="pass_png.png")
pass_label = Label(pack_frame, image=pass_image, bg="#9D8189")
pass_label.pack(padx=20, pady=20)

website_label = Label(grid_frame, text="Website: ", bg="#9D8189", font=("Helvetica", 12, "bold"))
website_label.grid(row=0, column=0)

entry_web = Entry(grid_frame, width=30)
entry_web.grid(row=0, column=1)
entry_web.insert(0, "Enter the Website Name")
entry_web.configure(state=DISABLED)

passgen_button = Button(grid_frame, text="Search", width=20, command=search)
passgen_button.grid(row=0, column=2, padx=10)

email_label = Label(grid_frame, text="Email/Username: ", bg="#9D8189", font=("Helvetica", 12, "bold"))
email_label.grid(row=1, column=0)

entry_email = Entry(grid_frame, width=30)
entry_email.grid(row=1, column=1)
entry_email.insert(0, "Enter Your Email/Username")
entry_email.configure(state=DISABLED)

password_label = Label(grid_frame, text="Password: ", bg="#9D8189", font=("Helvetica", 12, "bold"))
password_label.grid(row=2, column=0)

entry_pass = Entry(grid_frame, width=30)
entry_pass.grid(row=2, column=1, padx=10)
entry_pass.insert(0, "Enter Your Password")
entry_pass.configure(state=DISABLED)

passgen_button = Button(grid_frame, text="Generate Password", width=20, command=generate)
passgen_button.grid(row=2, column=2, padx=10)

add_button = Button(grid_frame, text="Add", width=70, command=save)
add_button.grid(row=3, column=0, pady=50, columnspan=3)


def on_click_web(event):
    entry_web.configure(state=NORMAL)
    entry_web.delete(0, END)
    entry_web.unbind('<Button-1>', on_click_id)


def on_click_email(event):
    entry_email.configure(state=NORMAL)
    entry_email.delete(0, END)
    entry_email.unbind('<Button-1>', on_click_id2)


def on_click_pw(event):
    entry_pass.configure(state=NORMAL)
    entry_pass.delete(0, END)
    entry_pass.unbind('<Button-1>', on_click_id3)


on_click_id = entry_web.bind('<Button-1>', on_click_web)
on_click_id2 = entry_email.bind('<Button-1>', on_click_email)
on_click_id3 = entry_pass.bind('<Button-1>', on_click_pw)

root.mainloop()
