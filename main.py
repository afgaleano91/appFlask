from flask import Flask

app = Flask(__name__)

#Se establece la ruta de index
@app.route('/')
def hello():
    return 'Hello world Flask'