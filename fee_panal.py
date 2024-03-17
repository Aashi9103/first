from tkinter import *
from tkcalendar import DateEntry
import pymysql as pq
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, showwarning

def connect_to_database():
    global mydb, mycursor
    mydb = pq.connect(host="localhost",user="root",
                    password="",database="Python_School")
    mycursor = mydb.cursor()


class fee_panal:

    def __init__(self):
        connect_to_database()
        mycursor.execute("""CREATE TABLE if not exists Student_fee_class_1(Roll_no int,Name varchar(50) , fee int , Date_of_fee_submission date)""")  
        mycursor.execute("""CREATE TABLE if not exists Student_fee_class_2(Roll_no int,Name varchar(50) , fee int , Date_of_fee_submission date)""")  
        mycursor.execute("""CREATE TABLE if not exists Student_fee_class_3(Roll_no int,Name varchar(50) , fee int , Date_of_fee_submission date)""")  
        mycursor.execute("""CREATE TABLE if not exists Student_fee_class_4(Roll_no int,Name varchar(50) , fee int , Date_of_fee_submission date)""")  
        mycursor.execute("""CREATE TABLE if not exists Student_fee_class_5(Roll_no int,Name varchar(50) , fee int , Date_of_fee_submission date)""")  
        mycursor.execute("""CREATE TABLE if not exists Student_fee_class_6(Roll_no int,Name varchar(50) , fee int , Date_of_fee_submission date)""")  
        mycursor.execute("""CREATE TABLE if not exists Student_fee_class_7(Roll_no int,Name varchar(50) , fee int , Date_of_fee_submission date)""")  
        mycursor.execute("""CREATE TABLE if not exists Student_fee_class_8(Roll_no int,Name varchar(50) , fee int , Date_of_fee_submission date)""")  
        mycursor.execute("""CREATE TABLE if not exists Student_fee_class_9(Roll_no int,Name varchar(50) , fee int , Date_of_fee_submission date)""")  
        mycursor.execute("""CREATE TABLE if not exists Student_fee_class_10(Roll_no int,Name varchar(50) , fee int , Date_of_fee_submission date)""")  
        mycursor.execute("""CREATE TABLE if not exists Student_fee_class_11(Roll_no int,Name varchar(50) , fee int , Date_of_fee_submission date)""")  
        mycursor.execute("""CREATE TABLE if not exists Student_fee_class_12(Roll_no int,Name varchar(50) , fee int , Date_of_fee_submission date)""")  



    def student_fee(self):
        Name = self.name.get()
        Roll  = self.roll.get()
        Fee = self.fee.get()
        Dob = str(self.date.get_date())
        table=str("student_data_class_"+str(self.selected_class.get()))
        mycursor.execute("SELECT * FROM " + table + " WHERE Name = '" + str(Name) + "'")
        data=mycursor.fetchall()
        
        mydb.commit()
        l = []
        for i in data:
            for j in i:
                l.append(j)
 
        if (Name != "") and (Roll != "") and (Fee != ""):
                if (str(Name) in l) and (int(Roll)  in l)  :
                    table=str("student_fee_class_"+str(self.selected_class.get()))
                    mycursor.execute(f'''INSERT INTO {table} (`Roll_no`, `Name`, `fee`, `Date_of_fee_submission`) VALUES ({Roll}, '{Name}', {Fee}, '{Dob}')''')
                    mydb.commit()
                    showinfo(title='Information', message='Fee Submit')
                else :
                    showerror(title='Error', message='Student is not Registered')
        else:
            showwarning(title='Warning',message='Please Fill All Mandatory Fields')

    def Student_fee_Panal(self):

        st_top = Toplevel()
        st_top.title("Fee_Panel ")
        window_width = 860
        window_height = 660

        screen_width = st_top.winfo_screenwidth()
        screen_height = st_top.winfo_screenheight()


        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)


        st_top.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        st_top.resizable(False, False)    



        font_panal = ("Time New Roam",25,"bold")
        font_panal1 = ("Time New Roam",20)
     
        bg_img = PhotoImage(file = "dem.png")
        l = Label(st_top,image = bg_img)
        l.place(x=0 ,y =0)
        
        
        Label(st_top,text = "Name*",font = font_panal,justify = tk.LEFT,bg = "yellow").place(x=100,y=50,height=50,width=300)
        Label(st_top,text = "Roll No*",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=150,height=50,width=300)
        Label(st_top,text = "Fee*",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=250,height=50,width=300)
        Label(st_top,text = "Date*",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=350,height=50,width=300)
        Label(st_top,text = "Class*",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=450,height=50,width=300)


        self.name = Entry(st_top,font = font_panal1)
        self.name.place(x=450,y=50,height=50,width=300)
        self.roll = Entry(st_top,font = font_panal1)
        self.roll.place(x=450,y=150,height=50,width=300)
        self.fee = Entry(st_top,font = font_panal1)
        self.fee.place(x=450,y=250,height=50,width=300)
        self.date = DateEntry(st_top,font = ("Time New Roam",15),selectmode='day',year=2021,month=8,day=17)
        self.date.place(x=450,y=350,height=50,width=300)

        self.selected_class = StringVar()
        self.class_s = ttk.Combobox(st_top, textvariable=self.selected_class,font = font_panal1,height=10)
        self.class_s['values'] = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        self.class_s.place(x=450,y=450,height=50,width=300)




      
        Button(st_top,text = "Submit",font= font_panal,bg= "blue",command = self.student_fee).place(width=300,height=50,x= 275,y = 550)
        
        st_top.mainloop()



# fee_panal().Student_fee_Panal()