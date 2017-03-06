from flask import Flask, flash, redirect, request, render_template, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector('frienddb')

@app.route('/')
def index():
    friends = mysql.fetch('SELECT * FROM friends')
    return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    hometown = request.form['hometown']
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(first_name, last_name, hometown)
    mysql.run_mysql_query(query)
    return redirect('/')

@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
    friend = mysql.fetch('SELECT * FROM friends WHERE id={}'.format(id))
    return render_template('friends.html', friend=friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    hometown = request.form['hometown']
    update = "UPDATE friends SET first_name='{}', last_name='{}', hometown='{}', updated_at=NOW() WHERE id={}".format(first_name, last_name, hometown, id)
    mysql.run_mysql_query(update)
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    delete = "DELETE FROM frienddb.friends WHERE id = {}".format(id)
    mysql.run_mysql_query(delete)
    return redirect('/')

app.run(debug=True)
