<h1 align="center">Microsoft Engage'22 Project
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/480px-Microsoft_logo.svg.png" alt="Logo" width="25" height="25">
</h1>

<p align="center">
  <a target="_blank" href="https://youtu.be/amwnQbqOSm0"><h2>Video Demo</h2></a>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Intoduction</a>
      <ul>
        <li><a href="#project-methodology">Project Methodology</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#agile-methodology">Agile Methodology</a>
      <ul>
        <li><a href="#what-is-agile">What is Agile</a></li>
        <li><a href="#how-i-incorporated-agile-methodology-during-the-development-cycle">How I Incorporated Agile Methodology During The Development Cycle</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#navigating-through-the-application">Navigating through the Application</a></li><ul>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->

## About The Project

The goal of this project is to identify history sheeters and provide a solution with
higher accuracy, better response rate and an initial step for video surveillance. Solution is proposed
based on nature of criminal psychic of repeating crime or involvement in it. This system is used to
track history sheeters and recognize them before and after any mischief or any unlawful activity.<br>

In the system I am storing the picture of criminal in the data set alongside its other detail to give 
ease in information recovery and ensuring fast deployment of results in real world. The project is built on
python with the use of OpenCV along with the algorithms like Haar cascade classifier, LBPH and
face_recognition etc. to store the detail of person we have used SQLite.<br>
 The human ability to remember and recognize faces is noteworthy. The system aims to provide a real-time copy of a human identifier along with personal details
for efficient tracking of history sheeters. The criminal face recognition system
creates a database of criminals and recognizes the person when their image matches an existing image in distributed environment
. This project will be a milestone in video-based facial recognition and
surveillance.<br><Br>
  <h2>Home Page</h2><br>
 <img src="https://user-images.githubusercontent.com/76876383/170870745-6776cb4d-04c9-42da-97c4-9e457ea77589.png" width="700"/>
  
  <!--Project Mthodology-->
## Project METHODOLOGY
  
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
  <img src="https://user-images.githubusercontent.com/76876383/170830883-e7777988-63d3-4c10-9de1-8d4aaabf2ef8.png" width="700"/>

  ### Built With

### Eagle_Criminal_Investigation_System: 
  
  <img src="https://user-images.githubusercontent.com/76876383/170869472-9b02dde6-7bf9-4685-8b81-9caf4c10942e.png" width="700"/>

  ## Tech Stack Used:
- OpenCV
- face_recognition
- Tkinter GUI
- Image module
- Numpy
- SQlite
- git
  
<!-- AGILE METHODOLOGY -->
## Agile Methodology

### What is Agile

Agile software development refers to software development methodologies centered around the idea of iterative development. Agile promotes teamwork, flexible procedures, and sle-organizing teams.

### How I Incorporated Agile Methodology During The Development Cycle

* Sprint 1 (May 5): Planning, Research and Design - Researching about various open source libraries and algorithms for face detection and recognition. After finalizing OpenCv and LBP, I searched for tutorials, designed a basic UI.

* Sprint 2 (May 13): Software development and debugging - Started the development process by taking help from YouTube tutorials. Built a machine learning model for the first time. Encountered occasional bugs which I debugged timely. Made required changes in the UI and color scheme to make it more eye pleasing

* Sprint 3 (May 19): Debugging and adding additional features - My research phase helped me in decide how to implement the surprise feature. Decided to build a Live Surveillance feature and integerate it in my application. Made changes styles and added log in authentication.
  
* Sprint 4 (May 25): Started debugging last moment bugs, collecting material for demo and finalising the project.
  

 <!-- INSTALLATIONS -->

## Getting Started
To install and run the project on your local system, following are the requirements:
 - Clone the GitHub repository
``` sh
$ git clone https://github.com/nandini7637/Eagle_Criminal_Investigation_System.git
```
 - Change directory to eagle_criminal_investigation_system
``` sh
$ cd Eagle_Criminal_Investigation_System/eagle_criminal_investigation_system
  ```
- Make sure to install the required dependencies from requirements.txt file
``` sh
 pip install -r requirements.txt 
```
### Installation
* Run the login.py file
 * username=nandini_ag
 * password = 123456 
  
  and voila you are ready to do some investigation!

  - NOTE: In case you face issue in installing dlib python package, follow the given steps: 
* pip install cmake
* Install Visual Studio build tools from here.
* In Visual Studio go to the Individual Components tab, Visual C++ Tools for Cmake, and check the checkbox under the "Compilers, build tools and runtimes" section.
pip install dlib

  -or
  
-Refer this video <a href="https://youtu.be/eaEndTeUiSU">Link</a>
  
   <h2><b><u>DETAILED PROCESS</u></b></h2>
   <u> <p> Import the required modules </p></u>
    <u> <p>  Load the face detection Cascade </p></u>
    <u> <p> Create the Face Recognizer Object</p></u>
    <u> <p> Prepare the training set and Perform the training </p></u>
   <u> <p> Testing  </p></u>
  
  
  <h1><b><u>Process flow diagram</u></b></h1>
  <img src="https://user-images.githubusercontent.com/76876383/170855447-cd6ed8b0-36d2-49c0-9a74-0d49bc1663d2.png">

<!-- APP TUTORIAL-->
## Navigating Through The Application
  
   <u> <h3> Login Page </h3></u>
  <img src="https://user-images.githubusercontent.com/76876383/170834987-c2286b46-0c75-45e5-a74a-9fb3282c802a.png">
  
   <u> <h3> Home Page </h3></u>
  <img src="https://user-images.githubusercontent.com/76876383/170870745-6776cb4d-04c9-42da-97c4-9e457ea77589.png" width="700"/>

  <u> <h3> Register Criminal </h3></u>
  <img src="https://user-images.githubusercontent.com/76876383/170852940-78000eb9-da0b-494d-bd01-d97d7e6fa817.png" width="700"/>
  
<u> <h3> Database Search </h3></u>
<img src="https://user-images.githubusercontent.com/76876383/170852993-1b2a6981-f9a6-4e27-8cd8-796b7ea34f44.png" width="700"/>
<img src="https://user-images.githubusercontent.com/76876383/170853021-2675aa51-500e-4ff5-b887-ed8f3b3a3e8e.png" width="700"/>
  
  <u> <h3> Live Surveillance </h3></u>
<img src="https://user-images.githubusercontent.com/76876383/170854674-b33f872c-b15c-4ae0-a8a6-872b9803d78a.png" width="700"/>

<h2><b><u>Future Scope of Improvements</u></b></h2>
-Light normalization may allow the threshold value to increase.<br>
-Improvement of face recognition using specific character in the face
 and also analyse the face in 3D by using more than one camera. Using
these two method the probability of error will decrease and system will be more accurate.
