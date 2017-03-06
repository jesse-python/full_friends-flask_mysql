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


app.run(debug=True)
