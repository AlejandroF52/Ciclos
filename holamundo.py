from flask import Flask
# This is a simple Flask application that returns "¡Hola, mundo!" when accessed at the root URL.

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo!'


if __name__ == '__main__':
    app.run(debug=True)