from flask import Flask, render_template, request
from ClassNode import Node
import sqlite3 as sql
app = Flask(__name__)
      

@app.route('/')
@app.route('/index/')
def home():
   return render_template('index.html')

@app.route('/enternew/')
def new_anedocte():
   return render_template('formulaire.html')

@app.route('/formulaire/',methods = ['POST', 'GET'])
def formulaire():
   if request.method == 'POST':
      pseudonyme=request.form['pseudo']
      pseudonyme = Node()
      return render_template('index.html')

      
@app.route('/BDD/')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("SELECT * FROM aned")
   
   rows = cur.fetchall();
   return render_template("VisuBDD.html",rows = rows)






   

if __name__ == '__main__' :
    app.run(debug = True)

