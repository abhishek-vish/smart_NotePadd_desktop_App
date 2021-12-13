from cx_Oracle import *
from traceback import *
class Db_Model:
    def __init__(self):
        self.file_dict = {}
        self.db_status = True
        self.conn = None
        self.cur = None

        try:
            self.conn = connect('Mojo/mojo@127.0.0.1/xe')
            print("Connected successfully to the DB")
            self.cur = self.conn.cursor()
        except DatabaseError:
            self.db_status = False
            print("DB Error:", format_exc())

obj = Db_Model()