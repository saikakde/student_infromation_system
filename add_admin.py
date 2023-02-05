from werkzeug.security import generate_password_hash
import mysql.connector as mysql
# from flask_sqlachemy import SQLAlchemy
from flask_wtf import FlaskForm
import sqlite3
from flask import session


class Admin():
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = generate_password_hash(password, 'sha256')
    
    def add(self):
        query = f'''
        INSERT INTO admin(username,password)
        VALUES ('{self.username}', '{self.password}')
        '''
        cursor.execute(query)
        db.commit()
        print('Admin added!')


if __name__ == '__main__':
    db = sqlite3.connect('sqlite_script.db')
    cursor = db.cursor()

    print('MySQL connection established!')
    print()
    print('For your SIS crendential')
    username = input("Username: ")
    password = input("Password: ")
    Admin(username,password).add()

# -----------------------------------------------
# class Admin(db.Model):
#     # def __init__(self, username, password) -> None:
#     #     self.username = username
#     #     self.password = generate_password_hash(password, 'sha256')
#     __tablename__ = 'admin'
#     uname = db.Column(db.String(20))
#     password = db.Column(db.String(20))
    
#     # def add(self):
#     #     query = f'''
#     #     INSERT INTO admin(username,password)
#     #     VALUE ('{self.username}', '{self.password}')
#     #     '''
#     #     cursor.execute(query)
#     #     db.commit()
#     #     print('Admin added!')
    


# if __name__ == '__main__':
#     print('To establish MySQL Connection')
#     # host = input("Enter your database host: ")
#     # user = input("Enter your database username: ")
#     # password = input("Enter your database password: ")

#     # db = mysql.connect(
#     #         host = host,
#     #         user = user,
#     #         password = password,
#     #         database = 'sisdb'
#     #     )

    
#     # db= SQLAlchemy(app)
#     cursor = db.cursor()
    
#     # cursor = db.cursor()

#     print('MySQL connection established!')
#     print()
#     print('For your SIS crendential')
#     username = input("Username: ")
#     password = input("Password: ")
#     # Admin(username,password).add()
#     user = Admin(username, password)
#     db.session.add(user)
#     db.session.commit()
    