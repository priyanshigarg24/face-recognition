#                          FACE RECOGNITION ATTENDANCE SYSTEM

## ABOUT THE PROJECT
It is a Desktop Application for:
- Tracking the attendance of a student using Face recognition
- Keeping a record of the attendance of a student
- Storing the details of the student and displaying the details by recognizing the face 

 ### Compatible platforms
- Laptops
- Desktops

### Built with
- BACK-END: mysql
- USER INTERFACE- python(tkkinter library)

### ALGORITHMS USED

Two algorithms have been used:

1. HAAR CASCADE ALGORITHM
   - Haar cascade algorithm is used for face detection.
   - It is an Object Detection Algorithm used to identify faces in an image or a real time video. The algorithm uses edge or line detection features.
 
2. LOCAL BINARY PATTERNS HISTOGRAMS ALGORITHM
   - Local Binary Pattern (LBP) is a very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel 
     and considers the result as a binary number.


## GETTING STARTED
To install and run the project on your local system, following are the requirements:

### PIP INSTALL THE LIBRARIES:
- opencv-contrib-python==4.5.5.64
- opencv-python==4.5.5.64
- mysql-connector-python==8.0.29
- numpy==1.22.4
- Pillow==9.1.1

### Connecting to Back-end
- mysql should be installed on your system and make a database "face_recognition" on mysql
(I have used MYSQL Workbench for making the database)
I have  username and password for mysql as "root" so change it accordingly in all the python files.

>create database face_recognition;

- create a table student
>CREATE TABLE `student` (
  `ID` int NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Course` varchar(45) DEFAULT NULL,
  `Dept` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `Sem` varchar(45) DEFAULT NULL,
  `DOB` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `Contact` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Photo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
);

- All the instructions for mysql queries is in a file "face_recognition_database.sql"

## Navigating Through The Desktop Application

### HOME WINDOW
Home Window has 6 buttons

<img width="955" alt="image" src="https://user-images.githubusercontent.com/78597231/170875136-0f264d7a-9176-4414-9565-f8e4e0b1c90c.png">

### STUDENTS DETAILS

After clicking on the student details button a new window will open for-
  - Displaying the details of the students.
  - Adding the details of a new student.
  - Updating the details of a student.
  - Deleting the details of a student.
  - By clicking on the "Take Photo Sample" button, web cam will open and capture images for training.

<img width="960" alt="image" src="https://user-images.githubusercontent.com/78597231/170875629-f3298f05-9dbe-4dad-9662-1f1e3ae20bab.png">

### TRAIN DATA

After clicking on the train data button a window will open with a button "start training data", after clicking on this button training of the data will start.
All the data will be stored in a folder "data".

<img width="958" alt="image" src="https://user-images.githubusercontent.com/78597231/170875847-e5acbeaa-0390-4e23-bd36-c96eaef9a0e2.png">

### FACE DETECTOR

After clicking on the face detector button a window will open with a button "star", after clicking on this button face Recognition will start.
After recognition of the face attendance will be stored in a csv file "attendance.csv".

<img width="949" alt="image" src="https://user-images.githubusercontent.com/78597231/170876013-abedbad6-13d4-4858-b4eb-981cb3d19341.png">

### PHOTOS

This button will open a folder "data" that has stored all the face dataset of the students that has been detected.

<img width="960" alt="image" src="https://user-images.githubusercontent.com/78597231/170876129-3503c590-ab13-48c5-b3c4-e690d889c75b.png">

### ATTENDANCE

This button will open a new window which shows the record of all the students that have been recognized by clicking on the "import csv" button which will redirect you to open a file. Select the file "attendance.csv" in the working directory and the details will be displayed on the screen

<img width="955" alt="111" src="https://user-images.githubusercontent.com/78597231/170876394-aa35071c-dcf2-4f80-afbe-18da490c12a1.png">

### EXIT 

Exit the home window by clicking on thi button

<img width="960" alt="image" src="https://user-images.githubusercontent.com/78597231/170876470-3c160a00-b962-4f0b-954c-262f1a1d7365.png">















