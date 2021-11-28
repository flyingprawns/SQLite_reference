# ============== Using just sqlite3 ================ #

# import sqlite3
#
# # CREATE DATABASE
# db = sqlite3.connect("books-collection.db")
#
# # CREATE CURSOR
# cursor = db.cursor()
#
# # CREATE A TABLE
# cursor.execute("CREATE TABLE books "
#                "(id INTEGER PRIMARY KEY, "
#                "title varchar(250) NOT NULL UNIQUE, "
#                "author varchar(250) NOT NULL, "
#                "rating FLOAT NOT NULL)")
#
# # ADD A BOOK TO TABLE
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


# ================ With SQLAlchemy ===================== #

# You will need to install SQLAlchemy with "pip3 install flask-SQLAlchemy"
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

