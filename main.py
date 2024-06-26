from flask import Flask
from routes.books import books_blueprint
from routes.proxy import proxy_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(books_blueprint)
app.register_blueprint(proxy_blueprint)

app.run("0.0.0.0", port=8001, debug=False)
