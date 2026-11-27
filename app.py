from flask import Flask, render_template
app = Flask(__name__)

@app.get("/login")

def login(): 
    return render_template("login.html")