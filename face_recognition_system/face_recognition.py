from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        #background image
        img1=Image.open(r"images/face2.jpeg")
        img1=img1.resize((1350,680),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img=Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1350, height=680)

        #button
        button_1=Button(bg_img, text="START",command=self.face_recog,cursor="hand2",font=("Times New Roman",30,"bold"),bg="light blue",fg="blue",justify=CENTER)
        #button_1.configure(activebackground="#33B5E5", relief = FLAT,justify=CENTER)
        button_1.place(x=100,y=500,width=520,height=100)
    
    ####attendance mark###
    def mark_attendance(self,i,n,c,d):
        with open("attendance.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            #no repeat attendance
            if((i not in name_list) and (n not in name_list) and (c not in name_list)and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{c},{d},{dstring},{d1},Present")



    

    #face recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scale_factor,min_neighbor,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scale_factor,min_neighbor)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                cursor_1=conn.cursor()
                
                cursor_1.execute("select Name from student where ID= "+str(id))
                n=cursor_1.fetchone() 
                n="+".join(n)  

                cursor_1.execute("select ID from student where ID= "+str(id))
                i=cursor_1.fetchone() 
                i="+".join(str(x) for x in i) 

                cursor_1.execute("select Course from student where ID= "+str(id))
                c=cursor_1.fetchone() 
                c="+".join(c)      

                cursor_1.execute("select Dept from student where ID= "+str(id))
                d=cursor_1.fetchone() 
                d="+".join(d) 


                
                if confidence>77 :
                    cv2.putText(img,f"Roll No:{i}",(x,y-100),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-70),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Course:{c}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dept:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,n,c,d)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()
    
      


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
