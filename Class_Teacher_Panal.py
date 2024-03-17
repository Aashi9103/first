from tkinter import *
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, showwarning
import pymysql as pq

mydb = pq.connect(host="localhost", user="root", password="",database='Python_School')
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists Python_School")

class class_teacher_control_panel:
    def Class_Teacher_Panal(self):
        st_top = Toplevel()
        st_top.title("Class_teacher_Panel ")
        font_panal = ("Time New Roman",25,"bold")
        font_panal1 = ("Time New Roman",20)
        
        bg_img = PhotoImage(file = "successful-college-student-lg.png")

        l = Label(st_top,image = bg_img)
        l.place(x=0 ,y =0)

        Label(st_top,text = "Name",font = font_panal,justify = tk.LEFT,bg = "yellow").place(x=100,y=50,height=50,width=300)
        Label(st_top,text = "ID",font = font_panal,justify = tk.LEFT,bg = "yellow").place(x=100,y=150,height=50,width=300)
        Label(st_top,text = "Class",font = font_panal,justify = tk.LEFT,bg = "yellow").place(x=100,y=250,height=50,width=300)
    
        self.name = Entry(st_top,font = font_panal1)
        self.name.place(x=450,y=50,height=50,width=300)
        self.id = Entry(st_top,font = font_panal1)
        self.id.place(x=450,y=150,height=50,width=300)
        self.selected_class = StringVar()
        self.class_s = ttk.Combobox(st_top, textvariable=self.selected_class,font = font_panal1,height=10)
        self.class_s['values'] = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        self.class_s.place(x=450,y=250,height=50,width=300)
        
        Button(st_top, text="Student Info Panel", font=font_panal, command=self.show_database).place(width=300, height=50, x=450, y=400)

        st_top.mainloop()


    def show_database(self):
        query=f''' SELECT * FROM teacher_database WHERE Class={self.class_s.get()} and Name='{self.name.get()}' and Id='{self.id.get()}' '''
        mycursor.execute(query)
        data=mycursor.fetchall()
        if self.class_s.get()==data[0]:
            st_top = Toplevel()
            st_top.geometry("850x600")
            st_top.resizable(False,False)
            st_top.title("New_Teacher_Join_Panel ")
            bg_img = PhotoImage(file = "successful-college-student-lg.png")
            Label(st_top,image = bg_img).place(x=0 ,y =0)

            tree = ttk.Treeview(st_top, columns=("Roll_no","Name","Father_Name","Mother_name","Phone_no","Date_of_Birth","Address","Cast"), show='headings')

            tree.heading('Roll_no', text='Roll_no')
            tree.heading('Name', text='Name')
            tree.heading('Father_Name', text='Father_Name')
            tree.heading('Mother_name', text='Mother_name')
            tree.heading('Phone_no', text='Phone_no')
            tree.heading('Date_of_Birth', text='Date_of_Birth')
            tree.heading('Address', text='Address')
            tree.heading('Cast', text='Cast')

            tree.column('Roll_no',width=100)
            tree.column('Name',width=100)
            tree.column('Father_Name',width=100)
            tree.column('Mother_name',width=100)
            tree.column('Phone_no',width=100)
            tree.column('Date_of_Birth',width=100)
            tree.column('Address',width=100)
            tree.column('Cast',width=100)


            query=f"SELECT * FROM student_data_class_{self.class_s.get()}"
            mycursor.execute(query)

            data=mycursor.fetchall()
            
            for i in data:
                tree.insert('', 'end', text='Parent', values=i)
            tree.place(x=0, y=0, width=850, height=600)

            st_top.mainloop()

        else:
            showerror(title="Error",message="No such teacher dataexist")