from flask import Flask, escape, request, jsonify, render_template
import sqlite3


conn = sqlite3.connect('user.db')

curs = conn.cursor()
#skapar table
#curs.execute("""CREATE TABLE user (
#    f_name text,
#    e_name text,
#    adress text,
#    postnummer integer,
#    ort text,
#    mobil integer,
#    epost text,
#    kommentar text
#)""")

#Lägger in i databasen
#curs.execute("INSERT INTO user VALUES ('Kristoffer','Palmgren','Ringen','76165','Borlange','0702602007','h19kripa@du.se','Hej')")

#Hämtar allt(*) från db
curs.execute("sELECT * FROM user")
#Hämtar allt i basen
print(curs.fetchall())

#lägger in i databasen
conn.commit()


curs.close()
