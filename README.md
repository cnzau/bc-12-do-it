# DO IT
Do IT is a To-do List Application done with python flask.

## Features
1. As a user I should be able to signup / login
2. As a user I should be able to create a list (Collection of Cards)
3. As a user I should be able to add a card to a list
  * I should be able to also move cards between lists
4. As a user I should be able to add the following to a card
  * A description
  * Several todo items
    - A user should be able to mark todo items as done
    - A user can also undo done tasks

## Live Demo
Deployed to Heroku. Click [here](https://do-it-py.herokuapp.com/) for demo.

## Contributors
* [Clement Nzau](https://github.com/cnzau)

## Requirements
* python 2.7
* SQLite
* pip

## Installation & Setup
1. Clone this repository to a directory.
    * Using HTTPS: git clone https://github.com/cnzau/do-it-py.git
    * Using an SSH Key: git clone git@github.com:cnzau/do-it-py.git
2. Navigate to the cloned directory ```do-it-py```
3. **Create** and **activate** a _**virtual environment**_.
   
   Instructions on how to install virtual environments are available [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
4. Run to install requirements: ```pip install -r requirements.txt```
5. Run the below to set up database:
  - ```python db_create.db```
  - ```python db_migrate.db```
6. Run the app: ```python run.py```
7. On your browser, type URL: ```http://localhost:5000/```

## Resources
* [Flask](http://flask.pocoo.org/)
* [Flask Book](https://flaskbook.com/)
* [The Flask Mega Tutorial](https://https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world/)
* [Python Docs](https://docs.python.org/2.7/)
* [Python’s SQLAlchemy](http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/)
* [ZURB Foundation](http://foundation.zurb.com/)

## Tools
* Trello
* Sublime
* Terminator
* Chrome developer tools
