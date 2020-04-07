from flask_sqlalchemy import SQLAlchemy

from PIL import Image

from models import *
# from faker import Faker

# from faker.providers import lorem

# fake = Faker()

# fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)

QUOTES = {'Walt Disney': 'The way to get started is to quit talking and begin \
    doing.', 'Nelson Mandela': 'The \
    greatest glory in living lies not in never falling, but in rising every\
    time we fall.', 'Eleanor Roosevelt': 'If life were predictable it would\
    cease to be life, and be without flavor.', 'James Cameron': 'If you set\
    your goals ridiculously high and it\'s a failure, you will fail above\
    everyone else\'s success.', 'John Lennon': 'Life is what happens when\
    you\'re busy making other plans.', 'Eleanor Roosevelt': 'The future belongs\
    to those who believe in the beauty of their dreams', 'Aristotle': 'It is\
    during our darkest moments that we must focus to see the light.', 'Anne\
    Frank': 'Whoever is happy will make others happy too.', 'Mother Teresa':\
    'Spread love everywhere you go. Let no one ever come to you without leaving\
    happier.', 'Margaret Mead': 'Always remember that you are absolutely\
    unique. Just like everyone else.', 'Nelson Mandela': 'The greatest glory in\
    living lies not in never falling, but in rising every time we fall.', 'Babe\
    Ruth': 'Never let the fear of striking out keep you from playing the\
    game.', 'Dalai Lama': 'The purpose of our lives is to be happy.', 'John\
    Lennon': 'Life is what happens when you\re busy making other plans.', 'Bob\
    Marley': 'Love the life you live. Live the life you love.'}

IMAGES = {'Walt Disney': 'static/images/waltDisney.jpeg',
    'Nelson Mandela': 'static/images/nelsonMandela.jpeg',
    'Eleanor Roosevelt': 'static/images/eleanorRoosevelt.jpeg',
    'James Cameron': 'static/images/jamesCameron.jpeg',
    'John Lennon': 'static/images/johnLennon.jpeg',
    'Aristotle:': 'static/images/aristotle.jpeg',
    'Margaret Mead': 'static/images/margaretMead.jpeg',
    'Babe Ruth': 'static/images/babeRuth.jpeg',
    'Dalai Lama': 'static/images/dalaiLama.jpeg',
    'Bob Marley': 'static/images/bobMarley.jpeg',
    'Mother Teresa': 'static/images/motherTeresa.jpeg',
    'Anne Frank': 'static/images/anneFrank.jpeg'}


# def seed():
# QUOTES = {'Author': 'Quote'}
def seed():

    for a, q in QUOTES.items():
        author = Author(name=a)
        author.save()

        quote = Quote(text=q, author_id=author.author_id)
        quote.save()

    print('Seeding successful.')


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    db.reflect()
    db.drop_all()
    db.create_all()

    seed()
    print('Data ready. Time to code!')
