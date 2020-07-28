from flask import Flask
app = Flask(__name__)
@app.route("/newscore")
def hello():
   return "Caio!"

@app.route("/ranking")
def hello():
   return "Caio!"

@app.route("/highscores")
def hello():
   return "Caio!"

@app.route("/")
def hello():
   return "Caio!"
