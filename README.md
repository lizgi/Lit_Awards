# Lit_Awards

### 11th Dec 2021

## Author  
  
~~ Elizabeth Gikonyo ~~
  
# Description  
Accolades is a platform where different creators get to  post their works,,,then they get to receive feedback based on certain criteria i.e,,design,usability and content,,.from the different reviewers.
  
##  Live Link  



 
## User Story  
  
* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

  
## Setup and Installation  

## Clone the repository:  
 
https://github.com/lizgi/lit_awards

## Navigate into the folder and install requirements 

 cd accolades pip install -r requirements.txt 

## Install and activate Virtual 

python3 -m venv virtual - source virtual/bin/activate  

##### Install Dependencies  
 
 pip install -r requirements.txt
 
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations photos
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8]
* [Django==3.2.9] 
* [Heroku]
  
  
## Known Bugs  
* There are no known bug


## License
MIT License

Copyright (c) 2021 lizgi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

