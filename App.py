from flask import Flask, render_template, request, redirect, url_for
import sqlite3 
app = Flask(__name__)
conn = sqlite3.connect('ThirlledMagerzine.db', check_same_thread = False)
conn.row_factory = sqlite3.Row

cursor = conn.cursor()
# Take the first page at frameword
@app.route('/', methods =['GET','POST'])
def HomePage():
    query = 'SELECT * FROM magerzines LIMIT 6'
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    return render_template('index.html', rows = rows)


app.run("0.0.0.0")