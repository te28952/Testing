from flask import *

import sqlite3
from flask_session.__init__ import Session


DATABASE = "IA2Databases.db"
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route('/')
def home():  # put application's code here
    return render_template("home.html")


@app.route('/cart')
def cart():
    return render_template("cart.html")


@app.route("/login", methods=["GET","POST"])
def login():
  if request.method =="POST":
    email = request.form.get("email")
    password = request.form.get("password")
     #get connection to database
    db = sqlite3.connect(DATABASE)
    #get a cursor to the database
    cursor = db.cursor()
    #5 create a query
    query = "SELECT * FROM users WHERE email = ? and password = ?"
    #6 create the data values to pass to the database
    values = (email, password)
    #7 get the results from the cursor to the database
    results = cursor.execute(query, values)
    #8get the first results from the cursor to our db
    user = results.fetchone()
    #9 close the pipe to the data base. pipe is the connection to the db
    db.close()
    if user:
      print(user)
      session["email"] = user[3]
      session["password"] = user[4]
      session["role"] = user[5]
      session["id"] = user[0]
      if session["role"] == "staff":
        return render_template("staff.html")
      if user:
        print(user)
        session["email"] = user[3]
        session["password"] = user[4]
        session["role"] = user[5]
        session["id"] = user[0]
        if session["role"] == "guest":
          return render_template("shop.html")
      else:
        return render_template("home.html")
    msg = "Incorrect username or password"
  return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method =="POST":
        FirstName = request.form.get("FirstName")
        LastName = request.form.get("LastName")
        email = request.form.get("email")
        password = request.form.get("password")
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        query = "INSERT INTO users (FirstName, LastName, email, password) VALUES(?,?,?,?)"
        values = (FirstName, LastName, email, password)
        cursor.execute(query, values)
        db.commit()
        db.close()
    return render_template("register.html")

@app.route('/staff')
def staff():
    return render_template("staff.html")
@app.route('/shop')
def shop():
    return render_template("shop.html")

@app.route('/stock')
def stock():
    return render_template("stock.html")

if __name__ == '__main__':
    app.run()
