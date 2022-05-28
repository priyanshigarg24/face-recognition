from cProfile import label
from logging import exception
from mimetypes import init
from re import L
from tkinter import *
from tkinter import ttk
from turtle import end_fill, width 
from PIL import Image,ImageTk 
from tkinter import messagebox
from matplotlib.pyplot import fill
from numpy import save
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        
        #background image
        img1=Image.open(r"images\bg.jpg")
        img1=img1.resize((1300,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img=Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1300, height=800)
        
        #left image
        head_img=Image.open(r"images\attendance.jpg")
        head_img=head_img.resize((540,540),Image.ANTIALIAS)
        self.photo_head_img=ImageTk.PhotoImage(head_img)

        head_lbl_img=Label(self.root, image=self.photo_head_img)
        head_lbl_img.place(x=50, y=85, width=540, height=535)
        

        #button
        button_frame=Frame(head_lbl_img,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=170,y=445,width=200,height=85)

        import_button=Button(button_frame,width=19,height=3,text="IMPORT CSV",command=self.importcsv,font=("times new roman",12,"bold"),bg="green",fg="white")
        import_button.grid(row=0,column=0,padx=5,pady=5)

        
        
        #title background img likho agr uske uppr dalna h to 
        title_lbl=Label(bg_img,text="STUDENT ATTENDANCE RECORD", font=("Times New Roman",40,"bold"),bg="white",fg="red",anchor=CENTER)
        title_lbl.place(x=0,y=0,width=1300,height=55)

        #rightframe
        right_frame=LabelFrame(bg_img,bd=2,bg="pink",relief=RIDGE,text="Attendance Record",font=("times new roman",12,"bold"))
        right_frame.place(x=650,y=80,width=540,height=540)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=10,width=510,height=490)

        #scroll bar
        scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendance_table=ttk.Treeview(table_frame,column=("ID","Name","Course","Dept","Time","Date","Attendance"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X) 
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.attendance_table.xview)
        scrolly.config(command=self.attendance_table.yview)
        
        self.attendance_table.heading("ID",text="Attendance ID")
        self.attendance_table.heading("Name",text="Name")
        self.attendance_table.heading("Course",text="Course")
        self.attendance_table.heading("Dept",text="Dept")
        self.attendance_table.heading("Time",text="Time")
        self.attendance_table.heading("Date",text="Date")
        self.attendance_table.heading("Attendance",text="Attendance")
        
        self.attendance_table["show"]="headings"

        self.attendance_table.column("ID",width=100)
        self.attendance_table.column("Name",width=100)
        self.attendance_table.column("Course",width=100)
        self.attendance_table.column("Dept",width=100)
        self.attendance_table.column("Time",width=100)
        self.attendance_table.column("Date",width=100)
        self.attendance_table.column("Attendance",width=100)
        
        self.attendance_table.pack(fill=BOTH,expand=1)

    ##fetch data
    def fetch_data(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)
    
    #data from csv file
    def importcsv(self):
        global mydata
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(filename) as myfile:
            csv_read=csv.reader(myfile,delimiter=",")
            for i in csv_read:
                mydata.append(i)
            self.fetch_data(mydata)




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()