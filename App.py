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
    query = 'SELECT * FROM podcast LIMIT 3'
    cursor.execute(query)
    chills = cursor.fetchall()
    print(chills)
    query = 'SELECT * FROM authors LIMIT 6'
    cursor.execute(query)
    authors = cursor.fetchall()
    print(authors)
    return render_template('index.html', rows = rows, chills = chills, authors = authors)


@app.route('/category', methods =['GET','POST'])
def CategoryPage():
    query= 'SELECT * FROM magerzines'
    cursor.execute(query)
    mager = cursor.fetchall()
    print(mager)
    query= 'SELECT * FROM podcast'
    cursor.execute(query)
    pod = cursor.fetchall()
    print(pod)

    return render_template('CategoryPage.html', mager = mager, pod = pod)

@app.route('/AdminPage', methods =['GET','POST'])
def AdminPage():
    query = 'SELECT * FROM magerzines'
    cursor.execute(query)
    mager = cursor.fetchall()
    print(mager)

    return render_template('AdminMagazine.html', mager= mager)

@app.route('/podcast', methods =['GET','POST'])
def PodcastPage():
    query = 'SELECT * FROM podcast LIMIT 6'
    cursor.execute(query)
    pod = cursor.fetchall()
    print(pod)

    return render_template('PodcastPage.html', pod= pod)
app.run("0.0.0.0", debug = True)