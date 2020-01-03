# 5Cpostman

## Description
This is a simple Flask application with a sqlite database created for the purpose of learning Get/Post/Put requests for RestfulAPIs.
It is not intended to be used in any production environment.  Users may use a GET request from url localhost:5000/car/{record id} or run
make a post request at url localhost:5000/car/post.  Input should be in JSON format and include model, year, color, and license_plate

``` Warning: Running project.py will start a web server on your computer ```
## Requirements
* Python 3.x
* Flask
* SQLAlchemy 
* SQLite browser Recommended 

### Additional task and known issues
There is little to no error handling, so invalid requests will fail with very little explanation 
There is no way to update or delete a record yet 
