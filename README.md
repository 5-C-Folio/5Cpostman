# 5Cpostman

## Description
This is a simple Flask application with a sqlite database created for the purpose of learning Get/Post/Put requests for RestfulAPIs.
It is not intended to be used in any production environment.  Users may use a GET request from url localhost:5000/car/{record id} or run
make a post request at url localhost:5000/car/post.  Input should be in JSON format and include model, year, color, and license_plate'

## Requirements
* Python 3.x
* Flask
* SQLAlchemy 
* SQLite browser Recommended 

## Instructions
1.  Install Python 3.x
2.  Create a new python virtual environment (not required but recommended)  <https://docs.python.org/3/library/venv.html> 
3. clone this repository 
4.  In your venv install requirments
5.  Execute database_setup.py to create the database
6.  When you execute project.py you will be running a webserver at port 5000.  
``` Warning: Running project.py will start a web server on your computer ```



### Additional task and known issues
There is little to no error handling, so invalid requests will fail with very little explanation 
There is no way to update or delete a record yet 
