#  Metric Helper

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Metric Helper by AU")
root.geometry("460x300")
root.resizable(0, 0)
root.iconbitmap("iconapp.ico")
root.config(background="#ffe4b8")

#  Font and Color
field_font = ("Palatino", 10)
button_color = "#E07A5F"


#  Define Functions
def convert():
    """Convert from one metric prefix to another"""
    metric_values = {
        "fento": 10 ** -15,
        "pico": 10 ** -12,
        "nano": 10 ** -9,
        "micro": 10 ** -6,
        "mili": 10 ** -3,
        "centi": 10 ** -2,
        "deci": 10 ** -1,
        "base value": 10 ** -0,
        "deca": 10 ** 1,
        "hecto": 10 ** 2,
        "kilo": 10 ** 3,
        "mega": 10 ** 6,
        "giga": 10 ** 9,
        "tera": 10 ** 12,
        "peta": 10 ** 15,
    }

    #  Clear the output field
    output_entry.delete(0, END)

    #  Get all user information
    user_input = float(input_entry.get())
    start_metric = input_combobox.get()
    end_metric = output_combobox.get()

    #  Convert to the base unit first
    start_value = user_input * metric_values[start_metric]
    end_value = start_value / metric_values[end_metric]

    #  Update output field
    output_entry.insert(0, str(end_value))


#  Define Layouts
#  Create the input and output fields
input_entry = Entry(root, font=field_font, width=30)
input_entry.grid(row=0, column=0, padx=10, pady=20)
input_entry.insert(0, "Enter the Quantity")
input_entry.configure(state=DISABLED)

equal_label = Label(root, text="=", font=field_font, background="#ffe4b8")
equal_label.grid(row=0, column=1, padx=10, pady=20)

output_entry = Entry(root, font=field_font, width=30)
output_entry.grid(row=0, column=2, padx=10, pady=20)


def on_click_input(event):
    input_entry.configure(state=NORMAL)
    input_entry.delete(0, END)
    input_entry.unbind('<Button-1>', on_click_id)


on_click_id = input_entry.bind('<Button-1>', on_click_input)

#  Create dropdowns for metric values
metric_list = ["base value", "fento", "pico", "nano", "micro", "mili", "centi", "deci", "deca", "hecto",
               "kilo", "mega", "giga", "tera", "peta"]

# Create combobox
input_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify="center")
input_combobox.grid(row=2, column=0)
input_combobox.set("base value")

to_label = Label(text="→", font=field_font, background="#ffe4b8")
to_label.grid(row=2, column=1)

output_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify="center")
output_combobox.grid(row=2, column=2)
output_combobox.set("base value")
# #  Create a dropdown menu using list
# variable = StringVar(root)
# variable.set("base value")
#
# input_dropdown = OptionMenu(root, variable, *metric_list)
# input_dropdown.grid(row=1, column=0)
#

#
# output_dropdown = OptionMenu(root, variable, *metric_list)
# output_dropdown.grid(row=1, column=2)

#  Create a conversion button
convert_button = Button(root, text="Convert", font=field_font, bg=button_color, command=convert)
convert_button.grid(row=3, column=1, pady=50)

root.mainloop()
