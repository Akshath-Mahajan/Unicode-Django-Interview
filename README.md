## UnicodeDjango

This Repository contains my solution to **Unicode Web Backend Assignment 2020 (Django)**

The directory 'UnicodeDjango' is the django project, which has implemented all four tasks (as per the requirement of the pdf)

On top of implementing different views for different tasks (as asked to), it has **also** compiled all the functionality of the website (all four tasks) on the homepage using **AJAX** calls.

The instructions are simple and mentioned on the homepage. For each task, you have the option of either going to the view to see the results, or loading the server's response directly on the homepage using **AJAX** calls

**Criteria Task 1:**

* [X] Input - Two Numbers
* [X] Output - Dictionary with numbers as keys and booleans as values

**Criteria Task 2:**

* [X] View that imports Task 1 and calls the function
* [X] Input supplied using parameters in *Dynamic URL*
* [X] Returns HTTPResponse

**Criteria Task 3:**

* [X] Create a view that will get input from a form
* [X] Query an API using the form values
* [X] Use the requests package of python to send a GET request to the API and get JSON data
* [X] Custom form built completely in the HTML template using the form tag and the Django {% url %} template tag

**Criteria Task 4:**

* [X] Create a database model and modify the view created in Task 3 to store all the
  successful requests made to the API and add an additional count field with default value 0
* [X] Create another view that will get input from a form for a specific field, query the database based on that
  specific field value and return the response on the same page
* [X] Every time the database is queried, update the count value for the objects matching that query by 1
* [X] Create a different page that will retrieve the top 3 values from the database based on their count
  values and display them using Django templates

---
