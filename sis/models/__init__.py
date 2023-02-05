import mysql.connector as mysql
from os import getenv
import sqlite3

# db = mysql.connect(
#             host = getenv('DB_HOST'),
#             user = getenv('DB_USERNAME'),
#             password = getenv('DB_PASSWORD'),
#             database = getenv('DB_NAME')
#         )
db = sqlite3.connect('sqlite_script.db')
cursor = db.cursor()
# cursor = db.cursor()



