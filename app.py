from flask import Flask, render_template

# Flask é um mine-framework (gerencia rotas)

app = Flask(__name__)

from api import bp
app.register_blueprint(bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
