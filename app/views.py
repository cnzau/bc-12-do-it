from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nzau'}  # fake user
    boards = [  # fake array of boards
        { 
            'creator': {'id': 1}, 
            'title': 'User creation' 
        },
        { 
            'creator': {'id': 1}, 
            'title': 'User auth' 
        }
    ]
    return render_template('index.html',
                           title='My To Do',
                           user=user,
                           boards=boards)
