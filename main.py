from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap

import unittest
from app import create_app
from app.forms import LoginForm

app = create_app()

todos = ['Comprar cafe', 'Entregar registro', 'Programar afiliaciones']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
    

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    # raise(Exception('500 error'))
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


#Se establece la ruta de index
@app.route('/hello', methods=['GET'])
def hello():
    user_ip = session.get('user_ip')
    username = session.get('username')

    context = {
        'user_ip' : user_ip,
        'todos' : todos,
        'username': username
    }

    return render_template('hello.html', **context)