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

###HOME WINDOW
<img width="955" alt="image" src="https://user-images.githubusercontent.com/78597231/170875136-0f264d7a-9176-4414-9565-f8e4e0b1c90c.png">





