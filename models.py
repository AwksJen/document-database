from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#############################################################################

class ModelMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()


class Author(ModelMixin, db.Model):
    __tablename__ = 'authors'

    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    quotes = db.relationship('Quote', backref='author')

    def __repr__(self):
        return f'<Author {self.author_id, self.name}>'


class Quote(ModelMixin, db.Model):

    __tablename__ = 'quotes'

    quote_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    text = db.Column(db.String(), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'))

    def __repr__(self):
        return f'<Quote {self.quote_id, self.text} >'


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///quotedb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    # db.drop_all()
    db.create_all()

    print('Connected to database, tables ready.')
