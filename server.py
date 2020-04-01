from views import app
from models import connect_to_db


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")

    connect_to_db(app)

    app.run()
