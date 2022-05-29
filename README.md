<h1><b><u>INTRODUCTION</u></b></h1>

Crime preventions and criminal identification are the primary issues for the police personnel, since
property and life protection are the basic concerns of the police but to combat the crime, the availability
of police personnel is limited.<br>

The goal of this project is to identify history sheeters and provide a solution with
higher accuracy, better response rate and an initial step for video surveillance. Solution is proposed
based on nature of criminal psychic of repeating crime or involvement in it. This system is used to
track history sheeters and recognize them before and after any mischief or any unlawful activity.<br>

In the system we are storing the picture of criminal in the data set alongside its other detail to give 
ease in information recovery and ensuring fast deployment of results in real world. The project is built on
python with the use of OpenCV along with the algorithms like Haar cascade classifier, LBPH and
face_recognition etc. to store the detail of person we have used SQLite.

The criminal record contains details about a particular individual, along with photos and personal
information. To identify a historian, you need to identify that person. One of the
's methods is face recognition. The face is the focus of our attention in social intercourse and plays an important
role in communicating identity and emotions. The human ability to remember and recognize faces is noteworthy. The system aims to provide a real-time copy of a human identifier along with personal details
for efficient tracking of history sheeters. The criminal face recognition system
creates a database of criminals and recognizes the person when their image matches an existing image in distributed environment
. This project will be a milestone in video-based facial recognition and
surveillance.<br><Br>
  <h2>Home Page</h2><br>
 <img src="https://user-images.githubusercontent.com/76876383/170829944-e0318820-0e84-4de7-97d6-ba7a8b7c76b5.png">
  
  <h1><b><u>METHODOLOGY</u></b></h1>
  
  <u> <h3> Face detection </h3></u>
I have used OpenCV, which represents the Haar cascade classifier used for face detection. The
Haar Cascade Classifier uses the AdaBoost algorithm to detect multiple facial features. First, it reads the detected image, converts it to a gray image, and then loads the Haar Cascade Classifier to determine if it contains a human face. If so, it examines facial features and draws a
rectangular frame on the detected face. Otherwise, the test for the next image will continue.<br>

   <p align="center">
  <img src="https://user-images.githubusercontent.com/76876383/170830273-0ffa4dd8-cba8-4f23-8b54-d5a8ff902676.png"><br>
  Haar cascade algorithm flowchart</p><br>
  
   <u> <h3> Face extraction & Identification  </h3></u>
  The LBP operator is used to describe the contrast information for a pixel and its adjacent pixels. The
original LBP operator is defined in the 3 * 3 window. The center pixel value is used as the window's
threshold and compared to the gray value of the adjacent 8 pixels. If you are in the neighborhood<br>
   <p align="center">
  <img src="https://user-images.githubusercontent.com/76876383/170830648-19dc288c-0c69-4226-94e8-5586c0daccae.png"><br>
  Basic LBP Operator</p><br>
  
  
   <u> <h3> SQLite </h3></u>
  SQLite is a software library that provides a relational database management system. SQLite lights mean lightweight in terms of setup, database management, and required resources.
SQLite has great features such as standalone, serverless, zero configuration and transaction.<br><br>
  <img src="https://user-images.githubusercontent.com/76876383/170830883-e7777988-63d3-4c10-9de1-8d4aaabf2ef8.png">


 <h1><b><u>PROCESS</u></b></h1>
   <u> <h3> Import the required modules </h3></u>
    <u> <h3>  Load the face detection Cascade </h3></u>
    <u> <h3> Create the Face Recognizer Object</h3></u>
    <u> <h3> Prepare the training set and Perform the training </h3></u>
   <u> <h3> Testing  </h3></u>
  
  <h1><b><u>Process flow diagram</u></b></h1>
  <img src="https://user-images.githubusercontent.com/76876383/170834215-184410f0-5e51-4af6-ba01-a286e55ea361.png">


<h1><b><u>RESULTS</u></b></h1>
  
   <u> <h3> Login Page </h3></u>
  <img src="https://user-images.githubusercontent.com/76876383/170834987-c2286b46-0c75-45e5-a74a-9fb3282c802a.png">
  
   <u> <h3> Home Page </h3></u>
  <img src="https://user-images.githubusercontent.com/76876383/170829944-e0318820-0e84-4de7-97d6-ba7a8b7c76b5.png">

  <u> <h3> Register Criminal </h3></u>
  <img src="https://user-images.githubusercontent.com/76876383/170852940-78000eb9-da0b-494d-bd01-d97d7e6fa817.png">
  
<u> <h3> Database Search </h3></u>
<img src="https://user-images.githubusercontent.com/76876383/170852993-1b2a6981-f9a6-4e27-8cd8-796b7ea34f44.png">
<img src="https://user-images.githubusercontent.com/76876383/170853021-2675aa51-500e-4ff5-b887-ed8f3b3a3e8e.png">
  
  <u> <h3> Live Surveillance </h3></u>
<img src="https://user-images.githubusercontent.com/76876383/170854674-b33f872c-b15c-4ae0-a8a6-872b9803d78a.png">

