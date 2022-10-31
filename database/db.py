import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS calculations (id INTEGER PRIMARY KEY, ship name, parameters, create_date, update_date, type)")
        self.con.commit()

    def insert(self, ship, parameters, creat_date, update_date, type):
        self.cur.execute(
            "INSERT INTO calculations VALUES (NULL, ?, ?, ?, ?, ?)",
            (ship, parameters, creat_date,
             update_date, type)
        )
        self.con.commit()

    def fetch(self):
        self.cur.execute('SELECT * FROM calculations')
        rows = self.cur.fetchall()
        return rows

    def fetch_one_row(self, id):
        self.cur.execute('SELECT * FROM calculations WHERE id =?', (id,))
        row = self.cur.fetchone()
        return row

    def remove_item(self, id):
        self.cur.execute("DELETE FROM calculations WHERE id = ?", (id,))
        self.con.commit()

    def get_id(self):
        self.cur.execute("SELECT last_insert_rowid()")
        id = self.cur.fetchone()
        return id[0]

    def update(self, id, ship, parameters, update_date, type):
        self.cur.execute("UPDATE calculations SET ship = ?, parameters = ?, update_date = ?, type = ? WHERE id= ?",
                         (ship, parameters, update_date, type, id))
        self.con.commit()

    def __del__(self):
        self.con.close()
