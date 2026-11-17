from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/dicas")
def dicas():
    return render_template("dicas.html")

@app.route("/desafios")
def desafios():
    return render_template("desafios.html")

@app.route("/curiosidades")
def curiosidades():
    return render_template("curiosidades.html")

if __name__ == "__main__":
    app.run(debug=True)
