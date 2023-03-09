#Mabon Ninan
#UC Dasec

import sqlite3
from flask import Flask, request, g, render_template, url_for, flash, redirect, session, send_file
import os


app = Flask(__name__)

DATABASE = 'database.db'

app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'qwerty'
app.config['UPLOAD_FOLDER'] = 'files/'


def connect_to_db():
    return sqlite3.connect(app.config['DATABASE'])

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = connect_to_db()
    return db

def user_info(rows):
    users = []
    for row in rows:
        users.append(
            {'username': row[2], 
             'password': row[3],
             'firstname': row[4],
             'lastname': row[5], 
             'email': row[6]}
            )
    return users

@app.route('/download')
def download():
    username = session['username']
    filename = os.path.join(app.config['UPLOAD_FOLDER'], f'{username}.txt')
    return send_file(filename, as_attachment=True, download_name='downloaded_file.txt')

@app.route('/viewinfo')
def viewinfo():
    username = session['username']
    rows = execute_query("""SELECT * FROM users WHERE username=?""", (username,))
    users = user_info(rows)
    with open(os.path.join(app.config['UPLOAD_FOLDER'], f'{username}.txt'), 'r') as f:
        data = f.read()
        num_words = len(data.split())
    return render_template('viewinfo.html', users=users, num_words=num_words)

@app.route('/login/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not (username and password):
            flash('Some field is missing, please check')
        else:
            rows = execute_query("""SELECT * FROM users WHERE username=? AND password=?""", (username, password))
            if len(rows) == 0:
                flash('Username or password incorrect')
            else:
                session['username'] = username
                return redirect(url_for('viewinfo'))
    return render_template('login.html')

@app.route('/register/', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        file = request.files['file']

        if not (username and password and firstname and lastname and email and file):
            flash('Some field is missing, Please fill in every field')
        elif execute_query("""SELECT * FROM users WHERE username=?""", (username,)) != []:
            flash('Username already existed, please choose a different one')
        else:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], f'{username}.txt'))
            flash('File successfully uploaded')
            execute_post("INSERT INTO users (username, password, firstname, lastname, email) VALUES (?,?,?,?,?)",
                        (username, password, firstname, lastname, email))
            session['username'] = username
            return redirect(url_for('viewinfo'))
    return render_template('register.html')

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
        
def execute_post(post, args=()):
    connection = get_db()
    connection.execute(post, args)
    connection.commit()
    connection.close()
    
def execute_query(query, args=()):
    cursor = get_db().execute(query, args)
    rows = cursor.fetchall()
    cursor.close()
    return rows

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

