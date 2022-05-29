from tkinter import *
from turtle import width
from PIL import ImageTk, Image
from subprocess import call
import time


def register():
    call(["python", "register.py"])


def LiveSurveillance():
    call(["python", "surveillance.py"])


def SearchDatabase():
    call(["python", "datasearch.py"])


if __name__ == "__main__":
    root = Tk()
    root.geometry('1200x750')
    root.minsize(1200, 750)
    root.maxsize(1200, 750)
    root.title("Eagle Criminal Identification System")
    root.configure(bg="white")
    heading = Frame(root)
    frame = Frame(root)
    result = Frame(root)


Fullname = StringVar()
father = StringVar()
var = IntVar()
c = StringVar()
d = StringVar()
var1 = IntVar()
file1 = ""
image = Image.open("content/c1.jpeg")
photo = ImageTk.PhotoImage(image)
photo_label = Label(image=photo, width=1200, height=0,
                    bg='white').place(x=0, y=0)
photo_label

# img = ImageTk.PhotoImage(Image.open("c1.jpeg"))
# img2 = ImageTk.PhotoImage(Image.open("c2.jpg"))
# img3 = ImageTk.PhotoImage(Image.open("c3.jpeg"))

# l = Label()
# l.pack()
# x = 1

# # function to change to next image


# def move():
#     global x
#     if x == 4:
#         x = 1
#     if x == 1:
#         l.config(image=img)
#     elif x == 2:
#         l.config(image=img2, width=0)
#     elif x == 3:
#         l.config(image=img3)
#     x = x+1
#     root.after(4000, move)


# # calling the function
# move()


def update():
    clock.config(text=time.strftime("%I:%M:%S"))
    clock.after(1000, update)


clock = Label(root, background='black', foreground='white',
              font=('arial', 40, 'bold'))
clock.pack()
update()

# label_0 = Label(root, text="Criminal Face Identification System", width=70, font=(
#     "bold", 20), anchor=CENTER, bg="#386184", fg="white")
# label_0.place(x=0, y=100)


Button(root, text='CRIMINAL REGISTERATION', width=45, height=5, bg='grey',
       fg='black', font=("bold", 13), command=register).place(x=750, y=180)
Button(root, text='SEARCH DATABASE', width=45, height=5, bg='grey', fg='black',
       font=("bold", 13), command=SearchDatabase).place(x=750, y=330)
Button(root, text='LIVE SURVEILLANCE', width=45, height=5, bg='grey',
       fg='black', font=("bold", 13), command=LiveSurveillance).place(x=750, y=480)


root.mainloop()
