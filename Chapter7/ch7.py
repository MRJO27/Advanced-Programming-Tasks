import sqlite3

# PROGRAM 1: Create Student Table and Insert Data
print("\n1) Creating school.db with student table")

con = sqlite3.connect('school.db')
curs = con.cursor()

curs.execute("CREATE TABLE IF NOT EXISTS student(ID INTEGER PRIMARY KEY, NAME TEXT, GRADE REAL)")

curs.execute("INSERT INTO student VALUES(20, 'MAZEN', 3)")
curs.execute("INSERT INTO student VALUES(50, 'VUSEF', 3)")
curs.execute("INSERT INTO student VALUES(30, 'MARI', 3)")

MYDATA = curs.execute("SELECT * FROM student")
print("\nAll students in database:")
for row in MYDATA:
    print(row)

con.commit()
con.close()


# PROGRAM 2: Interactive Student Data Entry

con = sqlite3.connect('school.db')
curs = con.cursor()

name = input("Enter name: ")
grade = float(input("Enter grade: "))

curs.execute("INSERT INTO student(name, grade) VALUES (?, ?)", (name, grade))

MYDATA = curs.execute("SELECT * FROM student")
rows = curs.fetchall()
print("\nAll students in database:")
for row in rows:
    print(row)

con.commit()
con.close()


# PROGRAM 3: Transaction with Rollback Example
conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade REAL)")

try:
    conn.execute("BEGIN")
    cur.execute("INSERT INTO students VALUES (1, 'All', 85.5)")
    cur.execute("INSERT INTO students VALUES (2, 'Sara', 92.0)")
    
    5 / 0
    
    conn.commit()
    print("Transaction committed successfully")
except:
    print("Error happened. Rolling back.")
    conn.rollback()

# Print final data
print("\nData in students table:")
for row in cur.execute("SELECT * FROM students"):
    print(row)

conn.close()



# PROGRAM 4: SQLAlchemy ORM Example
try:
    from sqlalchemy import create_engine, Column, Integer, String
    from sqlalchemy.orm import declarative_base, sessionmaker
    
    Base = declarative_base()
    
    class Book(Base):
        __tablename__ = "books"
        id = Column(Integer, primary_key=True)
        title = Column(String)
        author = Column(String)
    
    engine = create_engine("sqlite:///books.db")
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Add books
    b1 = Book(title="Python Basics", author="Guido")
    b2 = Book(title="AI with Python", author="Mohamed")
    session.add(b1)
    session.add(b2)
    session.commit()
    
    # Query and display books
    books = session.query(Book).all()
    print("\nBooks in database:")
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}")
    
    session.close()
    
except ImportError:
    print("SQLAlchemy is not installed. Install it using: pip install sqlalchemy")


import os

# Remove created database files
db_files = ["school.db", "students.db", "books.db"]
for db_file in db_files:
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Removed {db_file}")
    else:
        print(f"{db_file} not found")