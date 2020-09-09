from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


#Se establece la ruta de index
@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return f'Hello world Flask, your IP is {user_ip}'