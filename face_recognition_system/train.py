from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        #background image
        img1=Image.open(r"images/1.jpg")
        img1=img1.resize((1350,680),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img=Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1350, height=680)
        
        title_lbl=Label(bg_img,text="TRAIN DATA SET", font=("Times New Roman",35,"bold"),bg="black",fg="green",anchor=CENTER)
        title_lbl.place(x=0,y=0,width=1350,height=50)
        
        #button
                        
        button_1=Button(bg_img, text="START TRAINING DATA",command=self.train_classifier,cursor="hand2",font=("Times New Roman",18,"bold"),bg="black",fg="green",anchor=W)
        button_1.configure(activebackground="#33B5E5", relief = FLAT)
        button_1.place(x=750,y=280,width=280,height=70)
    
    def train_classifier(self):
        data_dir=("data")
        path =[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #converting to gray scale
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        #train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed",parent=self.root)
        


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()