from tkinter import *

# from tkcalendar import DateEntry
from Student_Panal import *
from fee_panal import *
from Principal_Panal import *
from Class_Teacher_Panal import *
import pymysql as pq


def Student_Panal_info():
    # Student_Panal()
    Student_Panal_class().Student_Panal()


def Student_Panal_fee():
    # fee_panal()
    fee_panal().Student_fee_Panal()


def class_teacher_panel():
    class_teacher_control_panel().Class_Teacher_Panal()


def principal_panel():
    Principal_Panal_class().Principal_Panal()


mydb = pq.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists Python_School")


win = Tk()

window_width = 850
window_height = 600

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()


center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)


win.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

win.resizable(False, False)

win.title("E - School")

bg_img = PhotoImage(file="homepage_banner_image.e32b007e.png")
Label(win, image=bg_img).place(x=0, y=0, height=600, width=850)

font_panal = ("Time New Roam", 20, "bold")

Button(win, text="Student Panel ", font=font_panal, command=Student_Panal_info).place(
    width=300, height=100, x=100, y=200
)

Button(win, text="Fee Panel ", font=font_panal, command=Student_Panal_fee).place(
    width=300, height=100, x=450, y=200
)

Button(
    win, text="Class Teacher Panel ", font=font_panal, command=class_teacher_panel
).place(width=300, height=100, x=100, y=350)

Button(win, text="Principal Panel ", font=font_panal, command=principal_panel).place(
    width=300, height=100, x=450, y=350
)

win.mainloop()
