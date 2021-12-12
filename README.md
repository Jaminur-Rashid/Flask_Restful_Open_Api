# Python_Web_Scraping
This is Restful Open API using Flask and Jwt that can search data by using keyword like hotel name, sleeping room, bedroom etc. from a local database 
from the Swagger UI. Data is sorted in ascending order of bedrooms. 


##### Project Features
* Can search Scraped hotel  properties like hotel name, sleeping, bedrooms, bathrooms ,locations etc.
* Implemented authentication using Jwt(Json Web Token)
* Data is sorted in ascending order of number of bedrooms

# Prerequisites
* Mysql
* Mysql Connector
* Python 3
* pip
* Previous project database(vrboDatabase)


# How the run the application
To run the application at first we have to install all the dependencies of the project

To install all the project dependencies run-
``` bash
pip install -r requirements.txt
now run the main.py script
```
After running the script it will redirect to the url below
```
http://127.0.0.1:5000/login
```
username : 
pasword  :1234

Copy the jwt token and visit -
```
http://127.0.0.1:5000/swaggerPage?token=Your Copied jwt token
```
Then you will be redirect to the swagger uI, and you can test the api from there.


# NOTE
As we have declared  database columns using varchar sorting of data is done by using string comparison.
To sort data by number comparison we only have to declare our ("Bedroom) columns as INT.
