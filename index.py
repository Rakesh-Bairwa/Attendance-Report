from tkinter import *
from PIL import ImageTk, Image
import csv

file = open('output.csv')
csvreader = csv.reader(file)
data = []
skip = 0
for row in csvreader:
    if (skip > 1):
        data.append(row)
    skip += 1
file.close()

def search():
    newWindow = Toplevel()
    newWindow.title("Search result")
    newWindow.geometry("700x500")

    NAME = str(name.get()).upper()
    
    bg = PhotoImage(file = "database.png")
    Label(newWindow, image = bg).place(x=0, y=0)
    
    for row in range(len(data)):
        if (data[row][0] == NAME.upper()):
            attendance_precentage = data[row][3]
            Label(newWindow, text =NAME + "  " + attendance_precentage, font=('Arial Bold', 18)).place(x=0, y=0)
            break
    newWindow.mainloop()

def database():
    Window = Toplevel()
    Window.title("Database")
    Window.geometry("760x500")
    
    scroll_bar = Scrollbar(Window)
    scroll_bar.pack(side = RIGHT, fill = Y)
    mylist = Listbox(Window, yscrollcommand = scroll_bar.set)
    
    for row in range(len(data)):
        attendance_precentage = data[row][3]
        mylist.insert(END, data[row][0] + "    :   " + attendance_precentage)
    
    mylist.pack(side = LEFT, fill = BOTH, expand=True)
    scroll_bar.config(command = mylist.yview)
    Window.mainloop()

def erase():
    name.delete(0, END)

root = Tk()
root.geometry("600x550")
root.title("Tkinter python project")

img = ImageTk.PhotoImage(Image.open("classroom.jpg"))
panel = Label(root, image = img)
panel.pack(side="bottom", fill="both", expand="yes")

Label(root, text='Enter Student Name', font=('Arial Bold', 18)).place(x=550, y=250)
name = Entry(root, font=('Arial Bold', 18))
name.place(x=525, y=325)

Button(root, text='Search', font=('Arial Bold', 18), activebackground='#669999', activeforeground='white', command=search).place(x=500, y=400)
Button(root, text='Clear', font=('Arial Bold', 18), activebackground='#669999', activeforeground='white', command=erase).place(x=620, y=400)
Button(root, text='Show All', font=('Arial Bold', 18), activebackground='#669999', activeforeground='white', command=database).place(x=720, y=400)

root.mainloop()
