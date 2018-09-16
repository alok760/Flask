from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_alok():
    return 'Hello, Alok!'

app.add_url_rule('/alok','/', hello_alok)

if __name__ == '__main__':
    app.run()
