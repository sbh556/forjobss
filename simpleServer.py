from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'hello %s1' % name

if __name__ == '__main__':
    app.run()
