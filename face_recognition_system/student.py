from cProfile import label
from logging import exception
from re import L
from tkinter import *
from tkinter import ttk
from turtle import width 
from PIL import Image,ImageTk 
from tkinter import messagebox
from matplotlib.pyplot import fill
from numpy import save
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_ID=StringVar()
        self.var_Name=StringVar()
        self.var_Course=StringVar()
        self.var_Dept=StringVar()
        self.var_Year=StringVar()
        self.var_Sem=StringVar()
        self.var_DOB=StringVar()
        self.var_Gender=StringVar()
        self.var_Contact=StringVar()
        self.var_Email=StringVar()
        self.var_Photo=StringVar()
        



        #header images
        head_img1=Image.open(r"images\student1.jpg")
        head_img1=head_img1.resize((400,120),Image.ANTIALIAS)
        self.photo_head_img1=ImageTk.PhotoImage(head_img1)

        head_lbl_img1=Label(self.root, image=self.photo_head_img1)
        head_lbl_img1.place(x=0, y=0, width=400, height=120)

        head_img2=Image.open(r"images\student2.jpg")
        head_img2=head_img2.resize((500,120),Image.ANTIALIAS)
        self.photo_head_img2=ImageTk.PhotoImage(head_img2)

        head_lbl_img2=Label(self.root, image=self.photo_head_img2)
        head_lbl_img2.place(x=400, y=0, width=500, height=120)

        head_img3=Image.open(r"images\student3.jfif")
        head_img3=head_img3.resize((400,120),Image.ANTIALIAS)
        self.photo_head_img3=ImageTk.PhotoImage(head_img3)

        head_lbl_img3=Label(self.root, image=self.photo_head_img3)
        head_lbl_img3.place(x=900, y=0, width=400, height=120)

        img1=Image.open(r"images\3.jpg")
        img1=img1.resize((1920,680),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img=Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=120, width=1920, height=680)

        #title background img likho agr uske uppr dalna h to 
        title_lbl=Label(bg_img,text="STUDENT DETAILS", font=("Times New Roman",35,"bold"),bg="black",fg="white",anchor=CENTER)
        title_lbl.place(x=0,y=0,width=1300,height=50)

         #frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1300,height=900)


        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Enter details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=600,height=450)
           
        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Course details",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=5,width=580,height=135)
        
        

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=0)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo['values']=("Select Course","B.Tech","M.Tech")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        
        #department
        dept_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dept_label.grid(row=0,column=2,padx=10)

        dept_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Dept,font=("times new roman",12,"bold"),width=17,state="readonly")
        dept_combo['values']=("Select Department","CSAI","CSE","IT","MAE","ECE")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo['values']=("Select Year","1","2","3","4")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=10, sticky=W)

        #semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Sem,font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_combo['values']=("Select Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #class student information
        student_info_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        student_info_frame.place(x=5,y=150,width=580,height=270)
        
        #student id
        studentID_label=Label(student_info_frame,text="Enrollment Number: ",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(student_info_frame,textvariable=self.var_ID,width=10,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        student_name_label=Label(student_info_frame,text="Student Name: ",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(student_info_frame,textvariable=self.var_Name,width=10,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #DOB
        dob_label=Label(student_info_frame,text="DOB: ",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(student_info_frame,textvariable=self.var_DOB,width=10,font=("times new roman",12,"bold"))
        dob_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #contact no.
        contact_label=Label(student_info_frame,text="Contact No: ",font=("times new roman",12,"bold"),bg="white")
        contact_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        contact_entry=ttk.Entry(student_info_frame,textvariable=self.var_Contact,width=10,font=("times new roman",12,"bold"))
        contact_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(student_info_frame,text="Email Address: ",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(student_info_frame,textvariable=self.var_Email,width=10,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #Gender
        gender_label=Label(student_info_frame,text="Gender: ",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(student_info_frame,textvariable=self.var_Gender,width=10,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        

        #radio buttons
        self.var_radio1=StringVar()
        radio_button1=ttk.Radiobutton(student_info_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio_button1.grid(row=6,column=0,padx=20,pady=10)

        
        radio_button2=ttk.Radiobutton(student_info_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio_button2.grid(row=6,column=1)

        #photo button frame
        photo_frame=Frame(student_info_frame,bd=2,relief=RIDGE,bg="white")
        photo_frame.place(x=20,y=150,width=520,height=35)

        take_photo_button=Button(photo_frame,text="Take Photo Sample", command=self.generate_dataset,width=27,font=("times new roman",12,"bold"), bg="light blue")
        take_photo_button.grid(row=0,column=0,padx=2)

        update_photo_button=Button(photo_frame,text="Update Photo Sample", command=self.generate_dataset,width=27,font=("times new roman",12,"bold"), bg="light blue" )
        update_photo_button.grid(row=0,column=1)
        
        
        
        #buttons frame

        button_frame=Frame(student_info_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=20,y=190,width=520,height=50)

        save_button=Button(button_frame,command=self.add_data,width=12,text="Save",font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0,padx=5,pady=5)

        update_button=Button(button_frame,width=12,text="Update",command=self.update_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1,padx=5,pady=5)

        delete_button=Button(button_frame,width=12,text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2,padx=5,pady=5)

        reset_button=Button(button_frame,width=12,text="Reset",command= self.reset_data,font =("times new roman",12,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3,padx=5,pady=5)





        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Details",font=("times new roman",12,"bold"))
        right_frame.place(x=670,y=10,width=580,height=450)
        
        #search system
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=5,width=560,height=70)
    
        search_label=Label(search_frame,text="Search by : ",font=("times new roman",12,"bold"),bg="light blue")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=10,state="readonly")
        search_combo['values']=("Select","Enrollment No","Phone No","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=10,font=("times new roman",15,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_button=Button(search_frame,width=9,text="search",font =("times new roman",12,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=5,pady=5)

        show_button=Button(search_frame,width=9,text="Show All",font =("times new roman",12,"bold"),bg="blue",fg="white")
        show_button.grid(row=0,column=4,padx=5,pady=5)

        #details frame
        details_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        details_frame.place(x=5,y=80,width=560,height=340)
        
        scrollx=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(details_frame,column=("ID","Name","Course","Dept","Year","Sem","DOB","Gender","Contact","Email","Photo"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.student_table.xview)
        scrolly.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="Enrollment No")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Dept",text="Department")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Contact",text="Contact No")
        self.student_table.heading("Email",text="Email Address")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Dept",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Contact",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Photo",width=100)

        
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #add data function
    def add_data(self):
        if self.var_Dept.get()=="Select Department" or self.var_Name.get()=="" or self.var_ID.get()=="" or self.var_Contact.get()=="" or self.var_Course.get()=="Select Course" or self.var_Year.get()=="Select Year" or self.var_Sem.get()=="Select Semester" or self.var_DOB.get()=="" or self.var_Email.get()=="" or self.var_Gender.get()=="" or self.var_Contact.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                cursor_1=conn.cursor()
                cursor_1.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                             self.var_ID.get(),
                                                                                             self.var_Name.get(),
                                                                                             self.var_Course.get(),
                                                                                             self.var_Dept.get(),
                                                                                             self.var_Year.get(),
                                                                                             self.var_Sem.get(),
                                                                                             self.var_DOB.get(),
                                                                                             self.var_Gender.get(),
                                                                                             self.var_Contact.get(),
                                                                                             self.var_Email.get(),
                                                                                             self.var_radio1.get()
                        
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

#fetch data in the right table
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
        cursor_1=conn.cursor()
        cursor_1.execute("select * from student")
        data=cursor_1.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_ID.set(data[0]),
        self.var_Name.set(data[1]),
        self.var_Course.set(data[2]),
        self.var_Dept.set(data[3]),
        self.var_Year.set(data[4]),
        self.var_Sem.set(data[5]),
        self.var_DOB.set(data[6]),
        self.var_Gender.set(data[7]),
        self.var_Contact.set(data[8]),
        self.var_Email.set(data[9]),
        self.var_radio1.set(data[10])

    #update function
    def update_data(self):
        if self.var_Dept.get()=="Select Department" or self.var_Name.get()=="" or self.var_ID.get()=="" or self.var_Contact.get()=="" or self.var_Course.get()=="Select Course" or self.var_Year.get()=="Select Year" or self.var_Sem.get()=="Select Semester" or self.var_DOB.get()=="" or self.var_Email.get()=="" or self.var_Gender.get()=="" or self.var_Contact.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                update_1=messagebox.askyesno("Update","Do you want to update?",parent=self.root)
                if update_1>0:

                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                    cursor_1=conn.cursor()
                    cursor_1.execute("update student set ID=%s,Name=%s, Course=%s,Dept=%s,Year=%s,Sem=%s,DOB=%s,Gender=%s,Contact=%s,Email=%s,Photo=%s where ID=%s",(self.var_ID.get(),self.var_Name.get(),self.var_Course.get(),self.var_Dept.get(), self.var_Year.get(), self.var_Sem.get(), self.var_DOB.get(), self.var_Gender.get(), self.var_Contact.get(), self.var_Email.get(),self.var_radio1.get(), self.var_ID.get()))

                else:
                    if not update_1:   
                        return  

                messagebox.showinfo("Sucess","Student details has been successfully updates",parent=self.root)                                                                       
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)                                                                                                                                                

    #delete function
    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Student Id is required",parent=self.root)
        else:
            try:
                delete_1=messagebox.askyesno("Student Delete Page","Do you want to delete the details?",parent=self.root)
                if delete_1>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                    cursor_1=conn.cursor()
                    sql="delete from student where ID=%s"
                    val=(self.var_ID.get(),)
                    cursor_1.execute(sql,val)
                else:
                    if not delete_1:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)        

    #reset function    
    def reset_data(self):
        self.var_ID.set(""),
        self.var_Name.set(""),
        self.var_Course.set("Select Course"),
        self.var_Dept.set("Select Department"),
        self.var_Year.set("Select Year"),
        self.var_Sem.set("Select Department"),
        self.var_DOB.set(""),
        self.var_Gender.set(""),
        self.var_Contact.set(""),
        self.var_Email.set(""),
        self.var_radio1.set("")

#generate dataset and take a photo sample
    def generate_dataset(self):

        if self.var_Dept.get()=="Select Department" or self.var_Name.get()=="" or self.var_ID.get()=="" or self.var_Contact.get()=="" or self.var_Course.get()=="Select Course" or self.var_Year.get()=="Select Year" or self.var_Sem.get()=="Select Semester" or self.var_DOB.get()=="" or self.var_Email.get()=="" or self.var_Gender.get()=="" or self.var_Contact.get()=="":

            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:

            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                cursor_1=conn.cursor()
                cursor_1.execute("select * from student")
                myresult=cursor_1.fetchall()
                id=0
                
                for x in myresult:
                    id+=1
                
                
                cursor_1.execute("update student set Name=%s, Course=%s,Dept=%s,Year=%s,Sem=%s,DOB=%s,Gender=%s,Contact=%s,Email=%s,Photo=%s where ID=%s",(self.var_Name.get(),self.var_Course.get(),self.var_Dept.get(), self.var_Year.get(), self.var_Sem.get(), self.var_DOB.get(), self.var_Gender.get(), self.var_Contact.get(), self.var_Email.get(),self.var_radio1.get(), self.var_ID.get()==id+1))
                    
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #load predefined data on face frontals from opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5
                    for (x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_crop(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_crop(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path=r"data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Dataset Successfully Generated")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)        






                    



                                                                                                                                       


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
   