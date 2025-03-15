from customtkinter import *
import tkinter
from main import *
import os

def validate_input(char, current_text):
    if not char.isdigit():
        return False
    if len(current_text) >= 11:
        return False
    return True
def closeapp():
    exit(0)
def write_Identity():

    humans = get_Identity()
    entry_name = StringVar()
    entry_surname = StringVar()
    entry_gender = StringVar()
    entry_id = IntVar()
    entry_country = StringVar()

    entry_name.set(humans[0])
    entry_surname.set(humans[1])

    if (humans[2] == 'E'):
        entry_gender.set("Erkek")
    elif (humans[2] == 'K'):
        entry_gender.set("Kadın")
    elif (humans[2] == 'U'):
        entry_gender.set("Erkek veya Kadın")
    else:
        entry_gender.set("Cinsiyet Bulunamadı")

    entry_id.set(humans[3])
    entry_country.set(humans[4])

    name.configure(textvariable=entry_name)
    surname.configure(textvariable=entry_surname)
    gender.configure(textvariable=entry_gender)
    person_id.configure(textvariable=entry_id)
    country.configure(textvariable=entry_country)

    print(humans[5])
    info.configure(text=humans[5])


root = CTk()
root.geometry("850x550+500+250")
root.resizable(width=False, height=False)
root.title("Fake Identity")
vcmd = (root.register(validate_input), '%S', '%P')
set_default_color_theme("green")
set_appearance_mode("system")

title = CTkLabel(master=root, text="Fake Identity Generator", font=("Arial", 32, "bold"))
title.pack(pady=25)

name = CTkEntry(master=root, placeholder_text_color="white" ,placeholder_text="Name...",font=("Arial", 18, "normal"), width=250, height=45)
name.place(relx=0.18, rely=0.2, anchor=tkinter.CENTER)

surname = CTkEntry(master=root, placeholder_text_color="white",placeholder_text="Surname...",font=("Arial", 18, "normal"), width=250, height=45)
surname.place(relx=0.18, rely=0.3, anchor=tkinter.CENTER)

gender = CTkEntry(master=root, placeholder_text_color="white",placeholder_text="Gender...",font=("Arial", 18, "normal"), width=250, height=45)
gender.place(relx=0.18, rely=0.4, anchor=tkinter.CENTER)

person_id = CTkEntry(master=root, placeholder_text_color="white",placeholder_text="123456789",font=("Arial", 18, "normal"), width=250, height=45, validatecommand=vcmd, validate='key')
person_id.place(relx=0.18, rely=0.5, anchor=tkinter.CENTER)

country = CTkEntry(master=root, placeholder_text_color="white",placeholder_text="Country",font=("Arial", 18, "normal"), width=250, height=45)
country.place(relx=0.18, rely=0.6, anchor=tkinter.CENTER)

info = CTkLabel(master=root, font=("Arial", 16, "normal"), width=10, height=150, wraplength=450, text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
info.place(relx=0.3, rely=0.82, anchor=tkinter.CENTER)

generateButton = CTkButton(master=root, text="Generate Identity", font=("Arial", 24, "bold")
                           ,corner_radius=8,border_width=0,width=150,height=45,command=write_Identity)
generateButton.place(relx=0.7, rely=0.15)

exitButton = CTkButton(master=root, text="Exit", font=("Arial", 24, "bold")
                           ,corner_radius=8,border_width=0,width=215,height=45,command=closeapp, fg_color="red", hover_color="#b00505")
exitButton.place(relx=0.7, rely=0.25)

reallabel = CTkLabel(master=root, text="No information is real.", text_color="red")
reallabel.place(relx=0.75, rely=0.35)


root.mainloop()