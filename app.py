from flask import Flask
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'DSC SRM Certificates Portal TOBE!'


if __name__ == '__main__':
    app.run()
