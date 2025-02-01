import uuid
from database.Database import connect, cursor

class Users:
    def __init__(self,  table="users"):
        self.table = table

    def _tblColumns(self, fields):
        return ", ".join(fields)

    def findAll(self, fields=("*"), join="", where=""):
        try:
            columns = self._tblColumns(fields)
            query = f"SELECT {columns} FROM {self.table} {join} {where}"
            cursor.execute(query)

            return cursor.fetchall()
        except Exception as e:
            raise Exception(f"Error fetching data: {e}")

    def findOne(self, fields=("*"), join="", where=""):
        try:
            columns = self._tblColumns(fields)
            query = f"SELECT {columns} FROM {self.table} {join} {where}"
            cursor.execute(query)

            return cursor.fetchone()
        except Exception as e:
            raise Exception(f"Error fetching data: {e}")
    
    
    def insert(self, values):
        try:
            query = f"INSERT INTO {self.table} VALUES (%s, %s, %s, %s, %s)"
            values.insert(0, str(uuid.uuid4()))
            cursor.execute(query, values)
            connect.commit()
        except Exception as e:
            raise Exception(f"Error inserting data: {e}")