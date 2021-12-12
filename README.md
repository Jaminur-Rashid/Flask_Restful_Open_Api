# Python_Web_Scraping
This is Restful Open API using Flask and Jwt that can search data by using keyword like hotel name, sleeping room, bedroom etc. from a local database 
from the Swagger UI. Data is sorted in ascending order of bedrooms. 


##### Project Features
* Can search Scraped hotel  properties like hotel name, sleeping, bedrooms, bathrooms ,locations etc.
* Implemented authentication using Jwt(Json Web Token)
* Data is sorted in ascending order of number of bedrooms

# Prerequisites
* Mysql
* Python 3
* pip
* Previous project database(vrboDatabase)

To install mysql connector run -
``` 
sudo apt-get install python3-mysql.connector
```

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


##### Database Table Structure
| ID             | Location       | Hotel_Name | Sleeping  | Bedroom | Bathroom | Price |
|----------------|----------------|------------|-----------|---------|----------|-------|
| uhg87-888-a7.  | Usa-Maryland   | Hotel One  | 10        | 3       | 2        | $60   |
| uhg87-888-a8.  | Usa-Maryland   | Hotel Two  | 6         | 2       | 3        | $127  |
| uhg87-888-a9.  | Usa-Maryland   | Hotel Three | 8         | 2       | 4        | $109  |
| uhg87-888-a10. | Usa-Maryland   | Hotel Four | 7         | 1       | 2        | $92   |
| uhg87-888-a11. | Usa-Maryland   | Hotel Five | 5         | 5       | 3        | $116  |
 | uhg87-88-a11.  | Usa-Maryland  |  Hotel Six | 2         | 4       | 1        | $225  |