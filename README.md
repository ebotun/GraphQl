# GraphQl
Python implementation of Graphql

## Setup (Powershell)

### Create env

    python -m venv graphql_venv

### Activate venv 

    .\graphql_venv\Scripts\Activate.ps1


### Install necessary dependencies

    pip install flask ariadne flask-sqlalchemy flask-cors requests psycopg2-binary 

### Database (Postgresql)

Create a database called `graphql`

    flask shell
    >>> from app import db
    >>> db.create_all()
    >>> exit()



### Run Server

    flask run

Api is accessible on localhost:5000


## Populate the database

### Run the .py in /requests

create -> createPost.py

delete -> deletePost.py

update -> updatePost.py

get post by id -> getPost.py

list all posts -> listPosts.py






