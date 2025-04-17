import mysql.connector

class Database:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="eshaa",
            password="esha123",
            database="sales"
        )
        self.cursor = self.con.cursor()

    def commit(self):
        self.con.commit()

    def close(self):
        self.cursor.close()
        self.con.close()