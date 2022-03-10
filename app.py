from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

#con = sqlite3.connect("coditas_emp.db")
#print("Database opened successfully")
#con.execute("drop table if exists Employee_data")
#con.execute("create table Employee_data (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, phone INTEGER(10) NOT NULL, address TEXT NOT NULL)")
#print("Table created successfully")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/savedetails", methods = ["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            address = request.form["address"]
            with sqlite3.connect("coditas_emp.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Employee_data (name, email, phone, address) values (?,?,?,?)",(name,email,phone,address))
                con.commit()
                msg = "Employee Added Successfully"
        except:
            con.rollback()
            msg = "Employee already exists!"
        finally:
            return render_template("success.html", msg = msg)
            con.close()


@app.route("/view")
def view():
    con = sqlite3.connect("coditas_emp.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Employee_data")
    rows = cur.fetchall()
    return render_template("view.html",rows = rows)


@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleterecord", methods = ["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("coditas_emp.db") as con:
        try: 
            cur = con.cursor()
            cur.execute("delete from Employee_data where id = ?", [id])
            msg = "Record deleted successfully!"
        except:
            msg = "Record can't be deleted"
        finally:
            return render_template("deletesuccess.html", msg = msg)


if __name__ == '__main__':
    app.run(debug=True)



    