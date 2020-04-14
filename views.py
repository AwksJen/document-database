import os

import random

from PIL import Image

from seed import QUOTES, IMAGES

from flask import Flask, render_template, request

# from models import Author, Quote

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secretzzz')


# app.secret_key = os.getenv('SECRET_KEY', 'secretzzz
@app.route('/')
def index():
    """Show the index."""

    return render_template('index.html')


@app.route('/random_quote')
def random_quote():

    r = random.choice(list(QUOTES.keys()))
    print(r)
    quote = QUOTES[r]
    image = IMAGES[r]
    return render_template('random_quote.html', quote=quote, author=r, image=image)


@app.route('/authored_quotes')
def authored_quotes():
    """Return authored-choice and single quote as a text string or multiple
       quotes as"""
    author = request.args.get('author')
    quote = QUOTES.get(author)
    image = IMAGES.get(author)

    return render_template('authored_quote-s.html', quote=quote, author=author, image=image)


@app.route('/authors_quotes')
def search_by_author():
    pass
    """Return authored-choice and single quote as a text string or multiple
       quotes as"""
    author = request.args.get('author')
    all_quotes = QUOTES.get(author)
    # list(QUOTES.keys())
   # for/if author=author
   # add its value to a new list object
    return render_template('authors_quotes.html', all_quotes=all_quotes, author=author)


@app.route('/authors')
def authors_list():
    """Return list of author possibilities"""
    # TODO: Create a new template and list all the authors on it.
    # authors = Author.query.all()
    authors_list = list(QUOTES.keys())

    return render_template('authors_list.html', authors_list=authors_list)


@app.route('/quotes')
def quotes_list():
    """ """
    quotes_list = list(QUOTES.values())

    return render_template('quotes_list.html', quotes_list=quotes_list)
