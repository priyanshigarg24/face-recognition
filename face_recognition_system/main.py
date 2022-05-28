from cProfile import label
from re import L
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import width 
from PIL import Image,ImageTk 
from tkinter import messagebox
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        
        img1=Image.open(r"images\3.jpg")
        img1=img1.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img=Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1920, height=1080)

        #title background img likho agr uske uppr dalna h to 
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("Times New Roman",35,"bold"),bg="black",fg="white",anchor=CENTER)
        title_lbl.place(x=0,y=0,width=1300,height=50)

        #buttons
        #button1=student details
        img2=Image.open(r"images\4.jpg")
        img2=img2.resize((180,180),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(bg_img, image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=180,height=180)

        b1_1=Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2",font=("Times New Roman",18,"bold"),bg="blue")
        b1_1.place(x=100,y=280,width=180,height=40)

        
        #button2=face detection
        img3=Image.open(r"images\2.jpg")
        img3=img3.resize((180,180),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b2=Button(bg_img, image=self.photoimg3,cursor="hand2",command=self.Face_Data)
        b2.place(x=500,y=100,width=180,height=180)

        b2_1=Button(bg_img, text="Face detector",cursor="hand2",command=self.Face_Data,font=("Times New Roman",18,"bold"),bg="blue")
        b2_1.place(x=500,y=280,width=180,height=40)


        #button3=attendance
        img4=Image.open(r"images\5.png")
        img4=img4.resize((180,180),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b3=Button(bg_img, image=self.photoimg4,cursor="hand2",command=self.attendance_Data)
        b3.place(x=900,y=100,width=180,height=180)

        b3_1=Button(bg_img, text="Attendance",cursor="hand2",command=self.attendance_Data,font=("Times New Roman",18,"bold"),bg="blue")
        b3_1.place(x=900,y=280,width=180,height=40)

        #button4= train data
        img5=Image.open(r"images\6.png")
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b4=Button(bg_img, image=self.photoimg5,cursor="hand2",command=self.train_data)
        b4.place(x=100,y=380,width=180,height=180)

        b4_1=Button(bg_img, text="Train Data",cursor="hand2",command=self.train_data,font=("Times New Roman",18,"bold"),bg="blue")
        b4_1.place(x=100,y=560,width=180,height=40)


        #button5= photos
        img6=Image.open(r"images\7.png")
        img6=img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b5=Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.open_images)
        b5.place(x=500,y=380,width=180,height=180)

        b5_1=Button(bg_img, text="Photos",cursor="hand2",command=self.open_images,font=("Times New Roman",18,"bold"),bg="blue")
        b5_1.place(x=500,y=560,width=180,height=40)

        #button6= Exit
        img7=Image.open(r"images\8.jpg")
        img7=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b6=Button(bg_img, image=self.photoimg7,cursor="hand2",command=self.window_exit)
        b6.place(x=900,y=380,width=180,height=180)

        b6_1=Button(bg_img, text="Exit",cursor="hand2",command=self.window_exit,font=("Times New Roman",18,"bold"),bg="blue")
        b6_1.place(x=900,y=560,width=180,height=40)

    
    #function buttons

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    #for photos button
    def open_images(self):
        os.startfile("data")

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def Face_Data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_Data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def window_exit(self):
        self.window_exit=messagebox.askyesno("Face Recognition","Do you want to exit?",parent=self.root)
        if self.window_exit>0:
            self.root.destroy()
        else:
            return

    


        




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()
   