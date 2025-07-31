from flask import Flask
app = Flask(__name__)

@app.route("/")
def olar():
    return "Hewwo Moindu Beluh!"

@app.route("/nome")
def nome():
    return "Kaio Emidio"

@app.route("/magica/<naosei>")
def magica(naosei):
    return naosei