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
   This web application allows the job seekers to get an idea about the Job titles and the respective salary in different States of America. To develop this application, 2022 Q4 data is used from the LCA disclosure  and converted from ecxel file to csv file format.I have used sqlite database for this project.The webpage is searching the database for the Job title as the user type-in the word and returns the Salary and the State.

   From the database I have used mainly three fields - Job Title, Wage and State.For future, we have also an option to add more details like the employers to this web application. I've used python code that automate the web application to lookup for the data.The results are returned in a row form. App.py is used to look up the database.GET method is used to send the search query to '/search' which in turn use the SQL to find the list of Job Titles that actually match.In the JavaScript code, we start by selecting the input box. Then, every time the input changes, I have used a function called fetch to get more data from the server without changing the URL of the current page.

   @app.route("/jobs")
   def jobs():

    q = request.args.get("q")
    if q:
        jobs = db.execute("SELECT JOB_TITLE, PREVAILING_WAGE, WORKSITE_STATE FROM jobs WHERE JOB_TITLE LIKE ? LIMIT 100", "%" + q + "%")
    else:
        jobs = []
    return jobs

   @app.route("/search")
   def search():

   return render_template("searched.html")


    <script>

        let input = document.querySelector('input');
        input.addEventListener('input', async function() {
            let response = await fetch('/jobs?q=' + input.value);
            let jobs = await response.text();
            dataObj = JSON.parse(jobs);
            let text = "<table class = 'table table-striped' id ='myTable'>" + "<tr>" + "<th onclick='sortTable(0)'>Job Title</th>" + "<th onclick='sortTable(1)'>Salary</th>"+ "<th onclick='sortTable(2)'>State</th>" + "</tr>"
            for (let x in dataObj) {
            text += "<tr>" + "<td>" + dataObj[x].JOB_TITLE + "</td>" + "<td>" +  dataObj[x].PREVAILING_WAGE +"</td>" + "<td>" + dataObj[x].WORKSITE_STATE + "</td>" + "</tr>";
            }
            text += "</table>"
            document.querySelector(".job-list").innerHTML=text;

        });


   Sorting feature is implement for this project.

          function sortTable(n) {


          var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
          table = document.getElementById("myTable");
          switching = true;
          //Set the sorting direction to ascending:
          dir = "asc";
          /*Make a loop that will continue until
          no switching has been done:*/
          while (switching) {
            //start by saying: no switching is done:
            switching = false;
            rows = table.rows;
            /*Loop through all table rows (except the
            first, which contains table headers):*/
            for (i = 1; i < (rows.length - 1); i++) {
              //start by saying there should be no switching:
              shouldSwitch = false;
              /*Get the two elements you want to compare,
              one from current row and one from the next:*/
              x = rows[i].getElementsByTagName("TD")[n];
              y = rows[i + 1].getElementsByTagName("TD")[n];
              /*check if the two rows should switch place,
              based on the direction, asc or desc:*/
              if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                  //if so, mark as a switch and break the loop:
                  shouldSwitch= true;
                  break;
                }
              } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                  //if so, mark as a switch and break the loop:
                  shouldSwitch = true;
                  break;
                }
              }
            }
            if (shouldSwitch) {
              /*If a switch has been marked, make the switch
              and mark that a switch has been done:*/
              rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
              switching = true;
              //Each time a switch is done, increase this count by 1:
              switchcount ++;
            } else {
              /*If no switching has been done AND the direction is "asc",
              set the direction to "desc" and run the while loop again.*/
              if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
              }
            }
          }
          }







