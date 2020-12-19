from flask import Flask, redirect, url_for, render_template, request, session #session追加

app = Flask(__name__)

app.secret_key = 'user'

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
  #データベースに情報を送るとき
  if request.method == "POST":
    user = request.form["nm"] #ユーザー情報を保存する
    session["user"] = user
    return redirect(url_for("user"))
  else: #情報を受け取るとき
    if "user" in session:
      return redirect(url_for("user"))
    return render_template("login.html")

@app.route("/user")
def user():
  if "user" in session:
    user = session["user"]
    return f"<h1>{user}</h1>"
  else:
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
  session.app("user", None)
  return redirect(url_for("login"))

if __name__ == "__main__":
  app.run(debug=True)