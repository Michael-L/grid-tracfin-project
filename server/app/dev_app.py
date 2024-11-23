import time

def home():
    print("Searches the database for entries, then displays them.")
    time.sleep(600)
    # db = get_db()
    # cur = db.execute("SELECT * FROM designated_person ORDER BY lastname;")
    # entries = cur.fetchall()
    # return render_template("index.html", entries=entries)

home()