import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS vehicles(
            id Integer Primary Key,
            regno text,
            name text,
            account text,
            email text,
            deviceid text,
            contact text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, regno, name, account, email, deviceid, contact):
        self.cur.execute("insert into vehicles values (NULL,?,?,?,?,?,?)",
                         (regno, name, account, email, deviceid, contact))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from vehicles")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from vehicles where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, regno, name, account, email, deviceid, contact):
        self.cur.execute(
            "update vehicles set regno=?, name=?, account=?, email=?, deviceid=?, contact=? where id=?",
            (regno, name, account, email, deviceid, contact, id))
        self.con.commit()
