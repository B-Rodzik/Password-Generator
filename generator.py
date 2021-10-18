import random
from tkinter import *

root = Tk()
root.title("Generator haseł")
root.geometry("500x300")


def generator_ran_pswd():
    
    pw_entry.delete(0, END)

    pw_lenght = int(my_entry.get())

    my_password = ""
    for i in range(pw_lenght):
        my_password += chr(random.randint(33,126))

    pw_entry.insert(0, my_password)


def clipper():
    pass

lf = LabelFrame(root, text="Długość hasła: ")
lf.pack(pady=20)

my_entry = Entry(lf, font=("Helvetica", 24), bd=0)
my_entry.pack(pady=20, padx=20)

pw_entry = Entry(root, text='', font=("Helvetica", 24))
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generuj hasło", command=generator_ran_pswd)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Skopiuj do schowka", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
