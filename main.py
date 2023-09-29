from tkinter import *
from tkinter import messagebox
import os


def set_entry_frame_color(widget, color):
    widget.tk_setPalette(background=color)


def set_entry_frame_color2(widget, color):
    widget.tk_setPalette(background=color)


window = Tk()
window.title("Secret Text")
window.geometry("400x600+800+200")
window.resizable(False, False)
window.config(background="#363636")
window.overrideredirect(True)

photo = PhotoImage(file="924905.png")
logo = photo.subsample(4, 4)

canvas = Canvas(window, width=400, height=120, borderwidth=0, relief="flat")
canvas.create_image(80, 80, image=logo)
canvas.config(background="#363636", relief="flat")
set_entry_frame_color(canvas, "Teal")
label3 = Label(text="Enter your topic title", font=('Arial', 13, "bold"), bg="#6e7b8b", width=23, anchor="w")
label3.place(x=172, y=59)

canvas.pack()

entry1 = Entry(width=14, font=("Helvetica", 17), cursor="ibeam")
entry1.focus_set()
entry1.config(bg="#dddddd", borderwidth=1)
set_entry_frame_color(entry1, "#ee4b50")
entry1.place(x=172, y=83)


def change_button_color(event):
    event.widget.config(bg="#ee4b50")


def restore_button_color(event):
    event.widget.config(bg="#a2b5cd")


def change_button_color1(event):
    event.widget.config(bg="#ee4b50")


def restore_button_color1(event):
    event.widget.config(bg="#6e7b8b")


def exit_func():
    window.destroy()


def textWriteFile():
    text = entry1.get()
    with open("TopSecretText.txt", "a"):
        text = text.upper()
        textbox.insert("end", text + "\n")
        textbox.focus_set()
    entry1.delete(0, END)


def text2WriteFile():
    text2 = textbox.get("1.0", END)
    with open("TopSecretText.txt", "a") as file:
        file.write(text2 + "\n")
        entry2.focus_set()


def showPass():
    if entry2.cget("show") == "":
        entry2.config(show="*")
        button6.config(text="Show Password")
    else:
        entry2.config(show="")
        button6.config(text="Hide Password")


def password():
    openpassword = entry2.get()
    file_line = "TopSecretText.txt"

    if openpassword == SavePassword:
        messagebox.showinfo("Successful", "Login Successful!")
        entry2.delete(0, END)
        os.startfile(file_line, "open")
    elif openpassword == "":
        messagebox.showinfo("Error", "Please enter your password and entry your password.")
        entry2.delete(0, END)
    else:
        messagebox.showerror("Error", "Incorrect Password!")
        entry2.delete(0, END)


def SavePassword():
    global SavePassword
    SavePassword = entry2.get()
    entry2.delete(0, END)
    if SavePassword == "":
        messagebox.showinfo("Error", "Please enter your password and save your password.")

    else:
        messagebox.showinfo("Success", "Password Saved!")


button1 = Button(window, width=14, background="#6e7b8b", height=2, borderwidth=0, text="SAVE TITLE",
                 font=("Coming Sono", 9,
                       "bold"), command=textWriteFile)
button1.place(x=0, y=123)
button2 = Button(window, command=text2WriteFile, width=14, background="#a2b5cd", height=2, borderwidth=0,
                 text="SAVE TEXT", font=("Coming Sono", 9,
                                         "bold"))
button2.place(x=100, y=123)
button3 = Button(window, width=14, background="#6e7b8b", height=2, borderwidth=0, text="BUTTON", font=("Coming Sono", 9,
                                                                                                       "bold"))
button3.place(x=198, y=123)
button4 = Button(window, width=14, background="#a2b5cd", height=2, borderwidth=0, text="EXIT", font=("Coming Sono", 9,
                                                                                                     "bold"),
                 command=exit_func)
button4.place(x=299, y=123)

button1.bind("<Enter>", change_button_color1)
button1.bind("<Leave>", restore_button_color1)

button2.bind("<Enter>", change_button_color)
button2.bind("<Leave>", restore_button_color)

button3.bind("<Enter>", change_button_color1)
button3.bind("<Leave>", restore_button_color1)

button4.bind("<Enter>", change_button_color)
button4.bind("<Leave>", restore_button_color)

textbox = Text(window)
textbox.configure(width=21, height=10, background="#dddddd", font=("Arial", 20, "bold"))
textbox.place(x="42", y=170)

pass_label = Label(text="Please enter your password", font=("Arial", 14, "bold"), width=33)
pass_label.config(bg="#6e7b8b")
pass_label.place(x=0, y=495)

entry2 = Entry(window)
entry2.config(width=29, font=("Helvetica", 15), bg="#dddddd", show="*")
entry2.place(x=41, y=524)

button5 = Button(text="Password Entry", command=password, bg="#6e7b8b", borderwidth=1, width=22,
                 font=("Arial", 9, "bold"))
button5.place(x=40, y=552)
button6 = Button(window, command=showPass, text="Show Password", bg="#6e7b8b", borderwidth=1, width=22,
                 font=("Arial", 9, "bold"))
button6.place(x=202, y=552)
button7 = Button(window, command=SavePassword, text="Save Password", bg="#6e7b8b", borderwidth=1, width=22,
                 font=("Arial", 9, "bold"))
button7.place(x=118, y=576)

window.mainloop()
