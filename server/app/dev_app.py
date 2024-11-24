import time
from db.database_connection import DatabaseConnection

class DevApp:
    def start(self):
        print("Searches the database for entries, then displays them.")
        connect = DatabaseConnection()
        connect.db_connection
        time.sleep(600)
        # db = get_db()
        # cur = db.execute("SELECT * FROM designated_person ORDER BY lastname;")
        # entries = cur.fetchall()
        # return render_template("index.html", entries=entries)

app = DevApp()
app.start()