from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'jake'}
    title = 'Home'
    #posts is a list of dictionaries
    posts = [
        {
            'user': {'username':'Jake'},
            'body': 'Source 1 header'
        },
        {
            'user': {'username':'Stan'},
            'body': 'Source 2 header'
        }
    ]

    return render_template('index.html',  title=title, user=user, posts=posts)

