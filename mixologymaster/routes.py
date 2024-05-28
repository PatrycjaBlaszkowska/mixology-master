from flask import Flask, render_template
from mixologymaster import app, db


@app.route("/")
def index():
    # Render index(home) page as landing page
    return render_template("index.html")

@app.route("/specs")
def specs():
    #Render specs(recipes) page
    return render_template("specs.html")

@app.route("/contact")
def contact():
    #Render contact page
     return render_template("contact.html")


@app.route("/login")
def login():
    #Render login page
     return render_template("login.html")

@app.route("/register")
def register():
    #Render register page
     return render_template("register.html")

