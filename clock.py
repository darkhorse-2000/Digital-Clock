from tkinter import *
# from tkinter.messagebox import showinfo
# from tkinter.filedialog import askopenfilename, asksaveasfilename
import time

root = Tk()
root.geometry("655x444")
root.title("Tik-Tok-Tik-Tok")
root.wm_iconbitmap("4.ico")

def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    AM_PM = time.strftime("%p")
    time_zone = time.strftime("%Z")

    my_label1.config(text=hour + ":" + minute +  ":" + second + " " + AM_PM)
    my_label1.after(1000, clock)

    my_label2.config(text=time_zone + " " + day)

def update():
    my_label1.config(text="New Text")

my_label1 = Label(root,text="", font=("Helvetica", 48), fg="green", bg="black")
my_label1.pack(pady=20)

my_label2 = Label(root,text="", font=("Helvetica", 14))
my_label2.pack(pady=10)

clock() # Calling the clock function
# my_label.after(5000, update)



root.mainloop()


"""SS"""
