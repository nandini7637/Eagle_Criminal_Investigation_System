from tkinter import *
import shutil
from PIL import ImageTk, Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
from subprocess import call


def callTrainer():
    call(["python", "modeltrain.py"])


if __name__ == "__main__":
    root = Tk()
    root.geometry('1350x720')
    root.minsize(1350, 720)
    root.configure(bg="#6c6e93")
    root.state("zoomed")
    root.title("Criminal Registration")


Fullname = StringVar()
Fathername = StringVar()
Mothername = StringVar()
Bodymark = StringVar()
dob = StringVar()
Nationality = StringVar()
Crime = StringVar()
gen = IntVar()
rel = StringVar()
blood = StringVar()
file1 = ""


image = Image.open("content/justice-lady.png")
resize_image = image.resize((500, 500))
photo = ImageTk.PhotoImage(resize_image)
photo_label = Label(image=photo, width=500, height=500).place(x=70, y=130)
photo_label

# image = Image.open("justice-lady.png")
# photo = ImageTk.PhotoImage(image)
# photo_label = Label(image=photo, width=0, height=0).place(x=0, y=0)
# photo_label


def ask():
    value = tmsg.askquestion(
        "CFIS WARNING !", "Select all (*) mandatory fields.\n(name,gender,religion,crime,pic)\n\n If done already, then proceed. \n\n Will you like to proceed ?")
    if value == "yes":
        x = databaseEnter()
        if(x == 1):
            tmsg.showinfo("Success", "New Face Recorded Successfully")
            root.destroy()
        else:
            tmsg.showinfo("Warning", "Please enter all (*) marked details")


def getid():
    conn = sqlite3.connect('criminal.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('select max(ID) from People')
    conn.commit()
    for row in cursor:
        for elem in row:
            x = elem
    return x


def databaseEnter():
    name = Fullname.get()
    father = Fathername.get()
    mother = Mothername.get()
    bl = blood.get()
    if(bl == "Select Blood Group"):
        bl = None
    body = Bodymark.get()
    nat = Nationality.get()
    crime = Crime.get()
    Dob = dob.get()
    gen1 = ""
    gender = gen.get()
    if(gender == 1):
        gen1 = 'Male'
    if(gender == 2):
        gen1 = 'Female'
    religion = rel.get()
    if(religion == "Select Religion"):
        religion = None

    if(name != "" and crime != "" and gen1 != ""):
        conn = sqlite3.connect('criminal.db')
        with conn:
            cursor = conn.cursor()
        #cursor.execute('CREATE TABLE IF NOT EXISTS People (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
        cursor.execute('INSERT INTO People (Name,Gender,Father,Mother,Religion,Blood,Bodymark,Nationality,Crime) VALUES(?,?,?,?,?,?,?,?,?)',
                       (name, gen1, father, mother, religion, bl, body, nat, crime))
        conn.commit()
        x = getid()
        file = "images/user." + str(x) + ".png"
        newPath = shutil.copy('temp/1.png', file)
    else:
        return 0
    return 1


def mfileopen():
    file1 = filedialog.askopenfilename()
    print(file1)
    newPath = shutil.copy(file1, 'temp/1.png')
    image = Image.open('temp/1.png')
    image = image.resize((500, 500), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    photo_label = Label(image=photo, width=500,
                        height=500).place(x=740, y=140).pack()
    label_ = Label(root, text=file1, width=70, font=("bold", 8))
    label_.place(x=260, y=630)


label_10 = Label(root, text="Criminal Registration Form", width=100, font=(
    "bold", 20), anchor=CENTER, bg="black", fg="white")
label_10.place(x=0, y=0)


##################  form begin  ######################

label_1 = Label(root, text="Name    *", width=20,
                font=("bold", 12), bg="black", fg="white")
label_1.place(x=740, y=140)

entry_1 = Entry(root, width=50, textvar=Fullname)
entry_1.place(x=930, y=140)

label_2 = Label(root, text="Father Name", width=20,
                font=("bold", 12), bg="black", fg="white")
label_2.place(x=740, y=190)

entry_2 = Entry(root, width=50, textvar=Fathername)
entry_2.place(x=930, y=190)

label_3 = Label(root, text="Gender      *", width=20,
                font=("bold", 12), bg="black", fg="white")
label_3.place(x=740, y=240)

Radiobutton(root, text="Male", padx=5, variable=gen,
            value=1).place(x=930, y=240)
Radiobutton(root, text="Female", padx=20,
            variable=gen, value=2).place(x=990, y=240)

label_4 = Label(root, text="Mother Name", width=20,
                font=("bold", 12), bg="black", fg="white")
label_4.place(x=740, y=290)
entry_5 = Entry(root, width=50, textvar=Mothername)
entry_5.place(x=930, y=290)

##############

label_4 = Label(root, text="Religion    *", width=20,
                font=("bold", 12), bg="black", fg="white")
label_4.place(x=740, y=340)
list1 = ['Hindu', 'Muslim', 'Buddhist', 'Christian', 'Sikh', 'Jain', 'Others']

droplist = OptionMenu(root, rel, *list1)
droplist.config(width=30)
rel.set('Select Religion')
droplist.place(x=930, y=335)


##########

label_5 = Label(root, text="Blood Group", width=20,
                font=("bold", 12), bg="black", fg="white")
label_5.place(x=740, y=380)

list2 = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-', 'Not known']

droplist = OptionMenu(root, blood, *list2)
droplist.config(width=30)
blood.set('Select Blood Group')
droplist.place(x=930, y=375)

label_6 = Label(root, text="Body Mark", width=20,
                font=("bold", 12), bg="black", fg="white")
label_6.place(x=740, y=415)

entry_6 = Entry(root, width=50, textvar=Bodymark)
entry_6.place(x=930, y=418)

label_7 = Label(root, text="Nationality", width=20,
                font=("bold", 12), bg="black", fg="white")
label_7.place(x=740, y=465)

entry_7 = Entry(root, width=50, textvar=Nationality)
entry_7.place(x=930, y=467)

label_8 = Label(root, text="Crime convicted        *",
                width=20, font=("bold", 12), bg="black", fg="white")
label_8.place(x=740, y=517)

entry_8 = Entry(root, width=50, textvar=Crime)
entry_8.place(x=930, y=519)

label_9 = Label(root, text="Face Image    *", width=20,
                font=("bold", 12), bg="black", fg="white")
label_9.place(x=740, y=567)

btn = Button(text="Select", width=20, command=mfileopen).place(x=930, y=569)
Button(root, text='Register', width=15, font=("bold", 10), bg='#15133C',
       height=2, fg='white', command=ask).place(x=900, y=600)

root.mainloop()
