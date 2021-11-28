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

# Create database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __rep__(self):
        return f'<Book {self.title}>'


db.create_all()

# # Create record
# new_book = Book(id=1, title="Harry Potter", author="J.K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

# # Read all records
# all_books = db.session.query(Book).all()

# # Read a specific record by QUERY
# book = Book.query.filter_by(title="Harry Potter").first()

# # Update a record by QUERY
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# # Update a record by PRIMARY KEY
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()

# # Delete a record by PRIMARY KEY
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
