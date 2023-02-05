from . import cursor
from werkzeug.security import check_password_hash
import sqlite3
db = sqlite3.connect('sqlite_script.db',check_same_thread=False)
cursor = db.cursor()
class Admin():
    def __init__(
        self,
        username: str = None,
        password: str = None) -> None:

        self.username = username
        self.password = password
        # self.password2 = password2

    
    def registered_user(self) -> bool:
        # return True
        query = f'''
            SELECT username, password 
            FROM admin
            WHERE username = '{self.username}';
        '''
        # flash('Wrong Credentials. Check Username and Password Again', category="error")
        cursor.execute(query)
        try:
            username, password = cursor.fetchone()
        except TypeError:
            return None
        if check_password_hash(password, self.password):
            return True

