from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
import pymysql as pq
from tkinter.messagebox import showwarning
from switch_to_priciple import *

mydb = pq.connect(host="localhost", user="root", password="", database="Python_School")
mycursor = mydb.cursor()


# In[2]:
class Principal_Panal_class:
    def __init__(self):
        mycursor.execute(
            """CREATE TABLE IF NOT EXISTS teacher_database (Class INT  PRIMARY KEY, Name VARCHAR(255), Id VARCHAR(255)) """
        )
        # for i in range(1, 13):
        #     mycursor.execute(f"""INSERT INTO teacher_database (Class, Name, Id) VALUES ({i},'x','0') """)
        #     mydb.commit()

    def verify_credential(self):
        if (
            self.Name.get() == "A"
            and self.id.get() == "1"
            and self.password.get() == "123"
        ):
            self.switch_to_principal_portal()

        else:
            showwarning(title="Invalid Data", message="Invalide username or data")

    def Principal_Panal(self):
        st_top = Toplevel()
        st_top.geometry("850x500")

        st_top.title("Principal_Admin_Panel ")
        font_panal = ("Time New Roam", 25, "bold")
        font_panal1 = ("Time New Roam", 20)

        bg_img = PhotoImage(file="successful-college-student-lg.png")
        Label(st_top, image=bg_img).place(x=0, y=0)

        Label(st_top, text="Name", font=font_panal, justify=tk.LEFT, bg="white").place(
            x=100, y=50, height=50, width=300
        )

        Label(
            st_top, text="Principal Id", font=font_panal, justify="left", bg="white"
        ).place(x=100, y=150, height=50, width=300)

        Label(
            st_top, text="Password", font=font_panal, justify="left", bg="white"
        ).place(x=100, y=250, height=50, width=300)

        self.Name = Entry(st_top, font=font_panal1)
        self.Name.place(x=450, y=50, height=50, width=300)

        self.id = Entry(st_top, font=font_panal1)
        self.id.place(x=450, y=150, height=50, width=300)

        self.password = Entry(st_top, font=font_panal1)
        self.password.place(x=450, y=250, height=50, width=300)

        Button(
            st_top,
            text="Submit",
            font=font_panal,
            bg="blue",
            command=lambda: self.verify_credential(),
        ).place(width=300, height=50, x=275, y=350)

        st_top.mainloop()

    def New_Teacher_Join(self):
        principal_control_panel().New_Teacher_Join()

    def Student_Info_Panel(self):
        principal_control_panel().Student_Info_Panel()

    def reset_teacher_db(self):

        # mycursor.execute(""" DROP TABLE IF EXISTS teacher_database """) 
        # mydb.close() 
        # mydb = pq.connect(host="localhost", user="root", password="", database="Python_School")
        # mycursor = mydb.cursor()
        # mycursor.execute(
        #     """CREATE TABLE IF NOT EXISTS teacher_database (Class INT  PRIMARY KEY, Name VARCHAR(255), Id VARCHAR(255)) """
        # )
        for i in range(1, 13):
            mycursor.execute("UPDATE teacher_database  SET  Name='x', Id='0' WHERE Class=%s", (i,))
            mydb.commit()

        # mydb.close()


    def show_teacher_db(self):
        principal_control_panel().show_teacher_db()

    def switch_to_principal_portal(self):
        st_top = Toplevel()
        st_top.geometry("850x600")
        st_top.resizable(False, False)
        st_top.title("Principal_Panel ")
        font_panal = ("Time New Roam", 25, "bold")
        font_panal1 = ("Time New Roam", 20)

        bg_img = PhotoImage(file="successful-college-student-lg.png")
        Label(st_top, image=bg_img).place(x=0, y=0)

        Button(
            st_top,
            text="New Teacher Join",
            font=font_panal,
            command=self.New_Teacher_Join,
        ).place(width=300, height=100, x=100, y=200)

        Button(
            st_top,
            text="Student Info Panel",
            font=font_panal,
            command=self.Student_Info_Panel,
        ).place(width=300, height=100, x=450, y=200)

        Button(
            st_top,
            text="Reset TeacherDB",
            font=font_panal,
            command=self.reset_teacher_db,
        ).place(width=300, height=100, x=100, y=400)

        Button(
            st_top,
            text="Show Teacher DB",
            font=font_panal,
            command=self.show_teacher_db,
        ).place(width=300, height=100, x=450, y=400)

        st_top.mainloop()
