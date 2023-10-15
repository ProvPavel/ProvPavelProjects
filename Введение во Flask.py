from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('frontend.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
