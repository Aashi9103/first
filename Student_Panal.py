from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import tkinter as tk
from tkinter.messagebox import showerror, showinfo, showwarning
import pymysql as pq

mydb = pq.connect(
        host="localhost",
        user="root",
        password="",
        database="Python_School")

mycursor = mydb.cursor()



class Student_Panal_class:

    def __init__(self):
       
        
        mycursor.execute("""CREATE TABLE if not exists Student_data_class_1 (Roll_no int NOT NULL AUTO_INCREMENT ,Name varchar(255),Father_Name varchar(255), 
            Mother_name varchar(255),Phone_no varchar(255),Date_of_Birth varchar(255),
            Address varchar(255),Cast varchar(255), PRIMARY KEY (Roll_no))""")  
      

        mycursor.execute("""CREATE TABLE if not exists Student_data_class_2 (Roll_no int NOT NULL AUTO_INCREMENT ,Name varchar(255),Father_Name varchar(255), 
            Mother_name varchar(255),Phone_no varchar(255),Date_of_Birth varchar(255),
            Address varchar(255),Cast varchar(255), PRIMARY KEY (Roll_no))""") 

        mycursor.execute("""CREATE TABLE if not exists Student_data_class_3 (Roll_no int NOT NULL AUTO_INCREMENT ,Name varchar(255),Father_Name varchar(255), 
            Mother_name varchar(255),Phone_no varchar(255),Date_of_Birth varchar(255),
            Address varchar(255),Cast varchar(255), PRIMARY KEY (Roll_no))""") 

        mycursor.execute("""CREATE TABLE if not exists Student_data_class_4 (Roll_no int NOT NULL AUTO_INCREMENT ,Name varchar(255),Father_Name varchar(255), 
            Mother_name varchar(255),Phone_no varchar(255),Date_of_Birth varchar(255),
            Address varchar(255),Cast varchar(255), PRIMARY KEY (Roll_no))""") 

        mycursor.execute("""CREATE TABLE if not exists Student_data_class_5 (Roll_no int NOT NULL AUTO_INCREMENT ,Name varchar(255),Father_Name varchar(255), 
            Mother_name varchar(255),Phone_no varchar(255),Date_of_Birth varchar(255),
            Address varchar(255),Cast varchar(255), PRIMARY KEY (Roll_no))""") 

        mycursor.execute("""CREATE TABLE if not exists Student_data_class_6 (Roll_no int NOT NULL AUTO_INCREMENT ,Name varchar(255),Father_Name varchar(255), 
            Mother_name varchar(255),Phone_no varchar(255),Date_of_Birth varchar(255),
            Address varchar(255),Cast varchar(255), PRIMARY KEY (Roll_no))""") 

        mycursor.execute("""CREATE TABLE if not exists Student_data_class_7 (Roll_no int NOT NULL AUTO_INCREMENT ,Name varchar(255),Father_Name varchar(255), 
            Mother_name varchar(255),Phone_no varchar(255),Date_of_Birth varchar(255),
            Address varchar(255),Cast varchar(255), PRIMARY KEY (Roll_no))""") 

        mycursor.execute("""CREATE TABLE if not exists Student_data_class_8 (Roll_no int NOT NULL AUTO_INCREMENT ,Name varchar(255),Father_Name varchar(255), 
            Mother_name varchar(255),Phone_no varchar(255),Date_of_Birth varchar(255),
            Address varchar(255),Cast varchar(255), PRIMARY KEY (Roll_no))""") 

        mycursor.execute("""CREATE TABLE if not exists Student_data_class_9 (Roll_no int NOT NULL AUTO_INCREMENT ,Name varchar(255),Father_Name varchar(255), 
            Mother_name varchar(255),Phone_no varchar(255),Date_of_Birth varchar(255),
            Address varchar(255),Cast varchar(255), PRIMARY KEY (Roll_no))""") 

        mycursor.execute("""CREATE TABLE if not exists Student_data_class_10 (Roll_no int NOT NULL AUTO_INCREMENT ,Name varchar(255),Father_Name varchar(255), 
            Mother_name varchar(255),Phone_no varchar(255),Date_of_Birth varchar(255),
            Address varchar(255),Cast varchar(255), PRIMARY KEY (Roll_no))""") 

        mycursor.execute("""CREATE TABLE if not exists Student_data_class_11 (Roll_no int NOT NULL AUTO_INCREMENT ,Name varchar(255),Father_Name varchar(255), 
            Mother_name varchar(255),Phone_no varchar(255),Date_of_Birth varchar(255),
            Address varchar(255),Cast varchar(255), PRIMARY KEY (Roll_no))""") 

        mycursor.execute("""CREATE TABLE if not exists Student_data_class_12 (Roll_no int NOT NULL AUTO_INCREMENT ,Name varchar(255),Father_Name varchar(255), 
            Mother_name varchar(255),Phone_no varchar(255),Date_of_Birth varchar(255),
            Address varchar(255),Cast varchar(255),PRIMARY KEY (Roll_no))""") 

        



    def class_table_data(self,table,Name_1):
        
  
        mycursor.execute("SELECT * FROM " + table + " WHERE Name = '" + str(Name_1) + "'")
        data=mycursor.fetchall()
        self.l = []
        for i in data:
            for j in i:
                self.l.append(j)

        return self.l

    def class_data_insert(self,x,y):


        mycursor.execute(f"SELECT Roll_no FROM {y} ORDER BY Roll_no DESC LIMIT 1")
        data_roll = mycursor.fetchone()
        try:
            roll_no=data_roll[0]+1
        except:
            roll_no=1


        mycursor.execute(f"""INSERT INTO {y}(Name,Father_Name,Mother_name,Phone_no,Date_of_Birth,Address,Cast) 
                 Values (%s,%s,%s,%s,%s,%s,%s)""",(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        mydb.commit()
        showinfo(title='Information', message=f'Successfully Registered Roll No : {roll_no}')    

    def student_info(self):        
        self.Name = str(self.name.get() + " " + self.lname.get())
        self.Fname  = self.fname.get()
        self.Mname = self.mname.get()
        self.Phone = self.phone_no.get()
        self.Dob = str(self.dob.get_date())
        self.Address =  self.address.get(1.0,END)
        self.Cast = self.selected_cast.get()
        self.Class = self.selected_class.get()

        self.st_data = [self.Name,self.Fname,self.Mname,self.Phone,self.Dob,self.Address,self.Cast]
        

        if (self.Name != "") and (self.Fname != "") and (self.Mname != "") and (self.Phone != "")  and (self.Address != "") and (self.Class != ""):
                self.table = str("student_data_class_"+self.Class)
                l = self.class_table_data(self.table,self.Name)
                if (self.Name not in l) and (self.Fname not in l) and (self.Mname not in l) and (self.Phone not in l)  and (self.Address not in l) :
                    self.class_data_insert(self.st_data,self.table)
                else :
                    showerror(title='Error', message='Student Already Registered')
        else:
            showwarning(title='Warning',message='Please Fill All Mandatory Fields')


    def Student_Panal(self):

        st_top = Toplevel()
        st_top.title("Student_Panel ")
        font_panal = ("Time New Roman",25,"bold")
        font_panal1 = ("Time New Roman",20)
        
        bg_img = PhotoImage(file = "successful-college-student-lg.png")
        l = Label(st_top,image = bg_img)
        l.place(x=0 ,y =0)
        
        Label(st_top,text = "Name*",font = font_panal,justify = tk.LEFT,bg = "yellow").place(x=100,y=50,height=50,width=300)
        Label(st_top,text = "Last Name*",font = font_panal,justify = tk.LEFT,bg = "yellow").place(x=800,y=50,height=50,width=300)

        Label(st_top,text = "Father Name*",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=150,height=50,width=300)
        Label(st_top,text = "Mother Name*",font = font_panal,justify = "left",bg = "yellow").place(x=800,y=150,height=50,width=300)

        Label(st_top,text = "Phone Number*",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=250,height=50,width=300)

        Label(st_top,text = "DOB*",font = font_panal,justify = "left",bg = "yellow").place(x=800,y=250,height=50,width=300)

        Label(st_top,text = "Class*",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=350,height=50,width=300)

        Label(st_top,text = "Cast*",font = font_panal,justify = "left",bg = "yellow").place(x=800,y=350,height=50,width=300)


        Label(st_top,text = "Address*",font = font_panal,justify = "left",bg = "yellow").place(x=100,y=450,height=100,width=300)
        
        

        self.name = Entry(st_top,font = font_panal1)
        self.name.place(x=450,y=50,height=50,width=300)

        self.lname = Entry(st_top,font = font_panal1)
        self.lname.place(x=1150,y=50,height=50,width=300)

        self.fname = Entry(st_top,font = font_panal1)
        self.fname.place(x=450,y=150,height=50,width=300)

        self.mname = Entry(st_top,font = font_panal1)
        self.mname.place(x=1150,y=150,height=50,width=300)

        self.phone_no = Entry(st_top,font = font_panal1)
        self.phone_no.place(x=450,y=250,height=50,width=300)

        self.dob = DateEntry(st_top,font = ("Time New Roman",15),selectmode='day',year=2021,month=8,day=17)
        self.dob.place(x=1150,y=250,height=50,width=300)

        self.selected_class = StringVar()
        self.class_s = ttk.Combobox(st_top, textvariable=self.selected_class,font = font_panal1,height=10)
        self.class_s['values'] = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        self.class_s.place(x=450,y=350,height=50,width=300)

        self.selected_cast = tk.StringVar()
        self.sizes = (('GEN', 'GEN'),('OBC', 'OBC'),('ST', 'ST'),('SC', 'SC'))


        self.r1 = Radiobutton(st_top,text=self.sizes[0][0],value=self.sizes[0][1],variable=self.selected_cast,font = font_panal1)
        self.r1.place(x=1150+0,y=350,height=50,width=100)

        self.r2 = Radiobutton(st_top,text=self.sizes[1][0],value=self.sizes[1][1],variable=self.selected_cast,font = font_panal1)
        self.r2.place(x=1150+110,y=350,height=50,width=100)

        self.r3 = Radiobutton(st_top,text=self.sizes[2][0],value=self.sizes[2][1],variable=self.selected_cast,font = font_panal1)
        self.r3.place(x=1150+0,y=410,height=50,width=100)

        self.r4 = Radiobutton(st_top,text=self.sizes[3][0],value=self.sizes[3][1],variable=self.selected_cast,font = font_panal1)
        self.r4.place(x=1150+110,y=410,height=50,width=100)

        self.address = Text(st_top,font = font_panal1)
        self.address.place(x=450,y=450,height=100,width=300) 
        
        self.button= Button(st_top,text = "Submit",font= font_panal,bg= "blue",fg= "white",command = self.student_info )
        self.button.place(width=300,height=50,x= 618,y = 700)
        
        st_top.mainloop()



# Student_Panal_class().Student_Panal()
