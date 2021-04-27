from flask import Flask, render_template, request
import sqlite3 as sql

class Node():
    def __init__(self):
              try:
                 self.pseudo = request.form['pseudo']
                 self.age = request.form['age']
                 self.anedocte = request.form['anedocte']
         
                 with sql.connect("database.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO aned (pseudo,age,anedoctes) VALUES (?,?,?)",(self.pseudo,self.age,self.anedocte) )
            
                    con.commit()
                    msg = "Record successfully added"
              except:
                 con.rollback()
                 msg = "error in insert operation"
      
              finally:
                 con.close()
        
