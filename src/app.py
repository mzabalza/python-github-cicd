from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return {'message': f'Hello World'}

@app.route("/name", methods=['GET'])
def index():
    return {'name': f'mikel'}
    
if __name__ == '__main__':
    app.run(debug=True)