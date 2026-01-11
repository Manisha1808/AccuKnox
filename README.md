# Assignmet Explanation

## Problem Statement 1

1) API Data Retrieval and Storage: You are tasked with fetching data from an external REST API, storing it in a local SQLite database, and displaying the retrieved data. The API provides a list of books in JSON format with attributes like title, author, and publication year.

Ans. I didn’t have any official API for books, so I used a public sample books API.
My logic was simple, first I fetched the data to just see what structure I get. It was a list of dictionaries, so I decided to store only the fields I actually needed: title, author, and year.
Instead of creating the database manually, I let Python create the SQLite file for me.
I used a very basic create table if not exists query because I didn’t want errors if I ran the script twice.
After that I just looped through the API response and inserted the records one by one.
Finally, I selected all the rows back from the database just to confirm that everything was inserted correctly.


2) Data Processing and Visualization: Given a dataset containing information about students' test scores, fetch the data from an API, calculate the average score, and create a bar chart to visualize the data.

Ans. I didn’t want to use random dummy APIs, so I uploaded the Kaggle dataset to my own GitHub and used the raw link as my external source.
This way, the data still comes from an external URL but I have control over it.
After loading the CSV using pandas, I noticed the dataset had three separate scores: math, reading, and writing. Instead of using only one subject, I calculated an average score for each student because that gives a better idea of their overall performance. Then I calculated the general average score of the whole dataset.
For the visualization part, I used matplotlib and created a simple bar graph using the index values as the x-axis since the dataset doesn’t have any unique student ID. The requirement only asked for a basic chart, so I didn’t add anything fancy.


3) CSV Data Import to a Database: Write a Python script that reads data from a CSV file containing user information (e.g., name, email) and inserts it into a SQLite database.

Ans. For the CSV import task, I created a small CSV file myself that only had name and email because that is enough to demonstrate the concept. I didn’t want to overcomplicate it.
I used Python’s built-in csv module since it’s very lightweight. While reading the file, I skipped the header using next(r) so I wouldn’t accidentally insert the column names into the database.
I also added a small check if len(row) == 2 because sometimes CSV files have empty lines and I didn’t want incomplete entries going into the database.
Once all the rows were inserted, I ran a simple select query just to confirm the data was actually stored.


Link 1(Python) : https://github.com/Manisha1808/Movie-Recommendation-System/blob/main/app.py

Link 2(SQL): https://github.com/Manisha1808/Pizza-sales-analysis/blob/main/Analysis.sql

