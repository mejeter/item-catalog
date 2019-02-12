from database_setup import Base, User, Genre, Movie
from flask import Flask, jsonify, request, redirect, render_template, url_for
from flask import flash, make_response
from flask import session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.pool import StaticPool

from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
import random
import string
import httplib2
import json
import requests


CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Item Catalog App"


app = Flask(__name__)


engine = create_engine(
    'sqlite:///movies.db',
    connect_args={'check_same_thread': False},
    poolclass=StaticPool)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/genre/JSON')
def genreJSON():
    """Return JSON to view all genres."""
    genres = session.query(Genre).all()
    return jsonify(genres=[g.serialize for g in genres])


@app.route('/genre/<int:genre_id>/movie/JSON')
def movieGenreJSON(genre_id):
    """Return JSON to view all movies within a given genre."""
    genre = session.query(Genre).filter_by(id=genre_id).one()
    movies = session.query(Movie).filter_by(genre_id=genre_id).all()
    return jsonify(Movies=[m.serialize for m in movies])


@app.route('/')
@app.route('/genre/')
def showGenres():
    """Show all genres."""
    genres = session.query(Genre).all()
    if 'username' not in login_session:
        return render_template('publicgenres.html', genres=genres)
    else:
        return render_template('genres.html', genres=genres)


@app.route('/genre/new/', methods=['GET', 'POST'])
def newGenre():
    """Add a new genre."""
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newGenre = Genre(
            name=request.form['name'], user_id=login_session['user_id'])
        session.add(newGenre)
        flash('New Genre %s Successfully Created' % newGenre.name)
        session.commit()
        return redirect(url_for('showGenres'))
    else:
        return render_template('newgenre.html')


@app.route('/genre/<int:genre_id>/edit/', methods=['GET', 'POST'])
def editGenre(genre_id):
    """Edit a genre."""
    editedGenre = session.query(Genre).filter_by(id=genre_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedGenre.user_id != login_session['user_id']:
        flash('You are not authorized to edit this genre.')
        return redirect(url_for('showGenres'))
    if request.method == 'POST':
        if request.form['name']:
            editedGenre.name = request.form['name']
            session.add(editedGenre)
            flash('%s Successfully Edited' % editedGenre.name)
            session.commit()
            return redirect(url_for('showGenres'))
    else:
        return render_template('editgenre.html', genre=editedGenre)


@app.route('/genre/<int:genre_id>/delete', methods=['GET', 'POST'])
def deleteGenre(genre_id):
    """Delete a genre."""
    genreToDelete = session.query(Genre).filter_by(id=genre_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if genreToDelete.user_id != login_session['user_id']:
        flash('You are not authorized to delete this genre.')
        return redirect(url_for('showGenres'))
    if request.method == 'POST':
        session.delete(genreToDelete)
        flash('%s Successfully Deleted' % genreToDelete.name)
        session.commit()
        return redirect(url_for('showGenres'))
    else:
        return render_template('deletegenre.html', genre=genreToDelete)


@app.route('/genre/<int:genre_id>/')
@app.route('/genre/<int:genre_id>/movie/')
def showMovies(genre_id):
    """Show all movies in a specific genre."""
    genre = session.query(Genre).filter_by(id=genre_id).one()
    admin = getUserInfo(genre.user_id)
    movies = session.query(Movie).filter_by(genre_id=genre_id).all()
    if 'username' not in login_session or admin.id != login_session['user_id']:
        return render_template(
            'publicmovies.html', movies=movies, genre=genre, admin=admin)
    else:
        return render_template(
            'movies.html', movies=movies, genre=genre, admin=admin)


@app.route('/genre/<int:genre_id>/movie/new', methods=['GET', 'POST'])
def newMovie(genre_id):
    """Add a new movie to genre."""
    genre = session.query(Genre).filter_by(id=genre_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if genre.user_id != login_session['user_id']:
        flash('You are not authorized to add movies to this genre.')
        return redirect(url_for('showMovies', genre_id=genre_id))
    if request.method == 'POST':
        newMovie = Movie(
            title=request.form['title'],
            year=request.form['year'],
            rating=request.form['rating'],
            plot_summary=request.form['plot_summary'],
            poster_image=request.form['poster_image'],
            genre=genre,
            user_id=login_session['user_id'])
        session.add(newMovie)
        flash('New Movie %s Successfully Created' % newMovie.title)
        session.commit()
        return redirect(url_for('showMovies', genre_id=genre_id))
    else:
        return render_template('newmovie.html', genre=genre)


@app.route(
    '/genre/<int:genre_id>/movie/<int:movie_id>/edit', methods=['GET', 'POST'])
def editMovie(genre_id, movie_id):
    """Edit a given movie."""
    genre = session.query(Genre).filter_by(id=genre_id).one()
    editedMovie = session.query(Movie).filter_by(id=movie_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedMovie.user_id != login_session['user_id']:
        flash('You are not authorized to edit this movie.')
        return redirect(url_for('showMovies', genre_id=genre_id))
    if request.method == 'POST':
        if request.form['title']:
            editedMovie.title = request.form['title']
        if request.form['year']:
            editedMovie.year = request.form['year']
        if request.form['rating']:
            editedMovie.rating = request.form['rating']
        if request.form['plot_summary']:
            editedMovie.plot_summary = request.form['plot_summary']
        if request.form['poster_image']:
            editedMovie.poster_image = request.form['poster_image']
        session.add(editedMovie)
        flash('%s Successfully Edited' % editedMovie.title)
        session.commit()
        return redirect(url_for('showMovies', genre_id=genre_id))
    else:
        return render_template(
            'editmovie.html',
            genre=genre,
            movie_id=movie_id,
            movie=editedMovie)


@app.route(
    '/genre/<int:genre_id>/movie/<int:movie_id>/delete',
    methods=['GET', 'POST'])
def deleteMovie(genre_id, movie_id):
    """Delete a movie."""
    genre = session.query(Genre).filter_by(id=genre_id).one()
    movieToDelete = session.query(Movie).filter_by(id=movie_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if movieToDelete.user_id != login_session['user_id']:
        flash('You are not authorized to delete this movie.')
        return redirect(url_for('showMovies', genre_id=genre_id))
    if request.method == 'POST':
        session.delete(movieToDelete)
        flash('%s Successfuly Deleted' % movieToDelete.title)
        session.commit()
        return redirect(url_for('showMovies', genre_id=genre_id))
    else:
        return render_template(
            'deletemovie.html',
            genre=genre,
            movie_id=movie_id,
            movie=movieToDelete)


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    """Use Google OAuth sign-in."""
    # Validate the state token.
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    code = request.data

    try:
        # Upgrade the authorization code into credentials.
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check whether the access token is valid.
    access_token = credentials.access_token
    url = (
        'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
        % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's ID."), 401)
        print "Token's client ID does not match app's ID."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps("Current user is already connected."), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info.
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # Check to see if user exists; if not, make a new user.
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px; border-radius: 150px; \
    -webkit-border-radius: 150px; style = "-moz-border-radius: 150px;">"'
    flash("You are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# User helper functions are below.
def createUser(login_session):
    newUser = User(
        name=login_session['username'],
        email=login_session['email'],
        picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception:
        return None


# Revoke current user's token and reset login session.
@app.route('/gdisconnect')
def gdisconnect():
    """ """
    # Disconnect a user only if they are already connected.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps("Current user not connected."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        del login_session['gplus_id']
        del login_session['access_token']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        flash("You have successfully logged out.")
        return redirect(url_for('showGenres'))
    else:
        response = make_response(
            json.dumps("Failed to revoke token for given user."), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = False
    app.run(host='0.0.0.0', port=8000)
