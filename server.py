from seed import QUOTES
from models import connect_to_db, db, Author, Quote
from views import app


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)

    app.run()
