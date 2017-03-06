from flask import Flask, flash, redirect, request, render_template, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector('frienddb')

@app.route('/')
def index():
    friends = mysql.fetch('SELECT * FROM friends')
    return render_template('index.html', friends=friends)


app.run(debug=True)
