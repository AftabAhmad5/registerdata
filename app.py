from flask import Flask, render_template, redirect, request
import sqlite3

# always always while inserting  name into table put it in single quotation as double quotation consider it as column of the table
# e-g INSERT INTO registrants(name, month, day) VALUES('abc',12,20); 

app = Flask(__name__)


@app.route("/")
def index():
    conn = sqlite3.connect("birthdays.db")
    db = conn.cursor()
    db.execute("SELECT * FROM registrants;")
    registrants = db.fetchall()
    conn.close()

    return render_template("index.html", registrants = registrants)



@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")
    # print(name, month,day)
    if name== '' or month == '' or day == '': # this line mean if someone is just submitting by not typing any thing then return and dont do anything.
        return redirect("/")
    conn = sqlite3.connect("birthdays.db")
    db = conn.cursor()
    db.execute("INSERT INTO registrants (name, month, day) VALUES (?,?,?)", (name, month, day))
    conn.commit() # save changes to the database
    conn.close() # close the database connection
    return redirect("/")

@app.route("/deregister", methods=["GET"])
def deregister():
    id  = request.args.get("id")
    id = int(id)
    print(id)
    print(type(id))

    conn = sqlite3.connect("birthdays.db")
    db = conn.cursor()
    if id:
        db.execute("DELETE FROM registrants WHERE id = ? ", (id,))
        conn.commit()
        conn.close()
    return redirect("/")
