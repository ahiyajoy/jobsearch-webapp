# CS50 Final project
### 2022 H1B JOBS IN USA
[Video demo](https://youtu.be/NvaveDMNeCw)

## Overview
 This is a simple web application to search by job title through H1B LCA database. For the purpose of this project I have used 2022 Q4 data, however this can be easily expanded to use data from more quarters and years.

## Tech stack
- Python flask web framework
- Front end: HTML, CSS, Javascript
- Backend: Python, Flask, SQLITE for database

## About the App
   This web application allows the job seekers to get an idea about the Job titles and the respective salary in different States of America. To develop this application, 2022 Q4 data is used from the LCA disclosure  and converted from ecxel file to csv file format. I have used sqlite database for this project. The webpage is searching the database for the Job title as the user type-in the word and returns the Salary and the State.

   From the database I have used mainly three fields - Job Title, Wage and State. For future, we have also an option to add more details like the employers to this web application. I've used python code that automate the web application to lookup for the data. The results are returned in a row form. App.py is used to look up the database. GET method is used to send the search query to '/search' which in turn use the SQL to find the list of Job Titles that actually match. In the JavaScript code, we start by selecting the input box. Then, every time the input changes, I have used a function called fetch to get more data from the server without changing the URL of the current page.

  
