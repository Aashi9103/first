from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
import pymysql as pq
from tkinter.messagebox import showwarning,showinfo
from switch_to_priciple import *
from tkinter import ttk

mydb = pq.connect(
        host="localhost",
        user="root",
        password="",
        database="Python_School")

mycursor = mydb.cursor()


class principal_control_panel:
    mycursor.execute('''CREATE TABLE IF NOT EXISTS teacher_database (Class INT  PRIMARY KEY, Name VARCHAR(255), Id VARCHAR(255)) ''')

    def New_Teacher_Join(self):
        st_top = Toplevel()
        st_top.geometry("850x600")
        st_top.resizable(False,False)
        st_top.title("New_Teacher_Join_Panel ")
        font_panal = ("Time New Roam",25,"bold")
        font_panal1 = ("Time New Roam",20)

        bg_img = PhotoImage(file = "successful-college-student-lg.png")
        Label(st_top,image = bg_img).place(x=0 ,y =0)

        Label(st_top,text = "Teacher Name",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=150,height=50,width=300)
        Label(st_top,text = "Teacher Id",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=250,height=50,width=300)
        Label(st_top,text = "Class",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=350,height=50,width=300)

        self.name = Entry(st_top,font = font_panal1)
        self.name.place(x=500,y=150,height=50,width=300)

        self.id = Entry(st_top,font = font_panal1)
        self.id.place(x=500,y=250,height=50,width=300)

        self.selected_class = StringVar()
        self.class_s = ttk.Combobox(st_top, textvariable=self.selected_class,font = font_panal1,height=10)
        self.class_s['values'] = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        self.class_s.place(x=500,y=350,height=50,width=300)


        Button(st_top,text = "Submit",font= font_panal,bg= "blue",command=lambda:self.insert_teacher_entry()).place(width=300,height=50,x= 300,y = 450)
        st_top.mainloop()


    def insert_teacher_entry(self):
        query=f''' UPDATE teacher_database SET Class={self.class_s.get()}, Name='{self.name.get()}', Id='{self.id.get()}' WHERE Class={self.class_s.get()} '''
        mycursor.execute(query)
        mydb.commit()

    def show_student_database(self):
        st_top = Toplevel()
        st_top.geometry("850x600")
        st_top.resizable(False,False)
        st_top.title("Student_Fee_info_Panel ")
        font_panal = ("Time New Roam",25,"bold")
        font_panal1 = ("Time New Roam",20)

        bg_img = PhotoImage(file = "successful-college-student-lg.png")
        Label(st_top,image = bg_img).place(x=0 ,y =0)

        Label(st_top,text = "Student Name",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=150,height=50,width=300)
        Label(st_top,text = "Roll_no",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=250,height=50,width=300)
        Label(st_top,text = "Class",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=350,height=50,width=300)
        
        self.name = Entry(st_top,font = font_panal1)
        self.name.place(x=500,y=150,height=50,width=300)

        self.roll = Entry(st_top,font = font_panal1)
        self.roll.place(x=500,y=250,height=50,width=300)

        self.s_class = StringVar()
        self.s_class = ttk.Combobox(st_top, textvariable=self.s_class,font = font_panal1,height=10)
        self.s_class['values'] = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        self.s_class.place(x=500,y=350,height=50,width=300)

        Button(st_top,text = "Submit",font= font_panal,bg= "blue",command=self.show_student__fee_table_data).place(width=300,height=50,x= 300,y = 450)
        

        st_top.mainloop()
    
    def show_student__fee_table_data(self):
        query=f''' SELECT * FROM student_fee_class_{self.s_class.get()} WHERE Name='{self.name.get()}' and Roll_no= {self.roll.get()} '''
        mycursor.execute(query)
        data=mycursor.fetchone()
        if data!= None:
            showinfo(title="Selected Student data",message=f" ROll no= {data[0]} \n Name={data[1]} \n Fee={data[2]} \n  Fess Submission Date={data[3]}")
        else:
            showwarning(title="Error", message="No such data found")


        

    def Student_Info_Panel(self):
        st_top = Toplevel()
        st_top.geometry("850x600")
        st_top.resizable(False,False)
        st_top.title("Student_Data_info_Panel ")
        font_panal = ("Time New Roam",25,"bold")
        font_panal1 = ("Time New Roam",20)
        
        bg_img = PhotoImage(file = "successful-college-student-lg.png")
        Label(st_top,image = bg_img).place(x=0 ,y =0)

        Button(st_top, text = "Student Fee",font= font_panal,command=self.show_student_database).place(width=300,height=100,x= 100,y = 200)
        Button(st_top, text = "Student Info",font= font_panal,command=self.show_student_Info_database).place(width=300,height=100,x= 500,y = 200)
        st_top.mainloop()

    def show_student_Info_database(self):
        st_top = Toplevel()
        st_top.geometry("850x600")
        st_top.resizable(False,False)
        st_top.title("Student_data_info_Panel ")
        font_panal = ("Time New Roam",25,"bold")
        font_panal1 = ("Time New Roam",20)

        bg_img = PhotoImage(file = "successful-college-student-lg.png")
        Label(st_top,image = bg_img).place(x=0 ,y =0)

        Label(st_top,text = "Student Name",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=150,height=50,width=300)
        Label(st_top,text = "Roll_no",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=250,height=50,width=300)
        Label(st_top,text = "Class",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=350,height=50,width=300)
        
        self.name = Entry(st_top,font = font_panal1)
        self.name.place(x=500,y=150,height=50,width=300)

        self.roll = Entry(st_top,font = font_panal1)
        self.roll.place(x=500,y=250,height=50,width=300)

        self.s_class = StringVar()
        self.s_class = ttk.Combobox(st_top, textvariable=self.s_class,font = font_panal1,height=10)
        self.s_class['values'] = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        self.s_class.place(x=500,y=350,height=50,width=300)

        Button(st_top,text = "Submit",font= font_panal,bg= "blue",command=self.show_student__data_table_data).place(width=300,height=50,x= 300,y = 450)
        st_top.mainloop()
    
    def show_student__data_table_data(self):
            query=f''' SELECT * FROM student_data_class_{self.s_class.get()} WHERE Name='{self.name.get()}' and Roll_no= {self.roll.get()} '''
            mycursor.execute(query)
            data=mycursor.fetchone()
            if data!= None:
                showinfo(title="Selected Student data",message=f'''
                          ROll no= {data[0]} 
                          Name={data[1]}
                          Father Name={data[2]}
                          Mother Name={data[3]}
                          Phone no={data[4]}
                          Date of Birth={data[5]}
                          Address={data[6]}
                          Cast={data[7]}
                          ''')
            else:
                showwarning(title="Error", message="No such data found")
        

    def show_teacher_db(self):
        st_top = Toplevel()
        st_top.geometry("850x600")
        st_top.resizable(False,False)
        st_top.title("New_Teacher_Join_Panel ")

        bg_img = PhotoImage(file = "successful-college-student-lg.png")
        Label(st_top,image = bg_img).place(x=0 ,y =0)

        tree = ttk.Treeview(st_top, columns=('Class', 'Name', 'Id'), show='headings')

        tree.heading('Class', text='Class')
        tree.heading('Name', text='Name')
        tree.heading('Id', text='Id')

        tree.column('Class', width=100)
        tree.column('Name', width=100)
        tree.column('Id', width=100)

        query="SELECT * FROM teacher_database"
        mycursor.execute(query)

        data=mycursor.fetchall()
        
        for i in data:
            tree.insert('', 'end', text='Parent', values=i)
        tree.place(x=0, y=0, width=850, height=600)

        st_top.mainloop()