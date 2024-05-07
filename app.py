from flask import Flask

# Flask é um mine-framework (gerencia rotas)

app = Flask(__name__)

from api import bp
app.register_blueprint(bp)

