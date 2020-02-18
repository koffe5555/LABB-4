import module
import http.server
from flask import Flask, render_template, jsonify, request
  
app = Flask(__name__, template_folder="template")

test = jsonify

#@app.route('/hello/<name>')
#def hello(name):
#   return render_template('hello.html', name=name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET'])
def register():
    # debug in console
    print(request.form.values)
    # send back to client
    return render_template('index.html')

@app.route('/', methods=['POST'])
def post():
    print(request.form.values)
    return render_template('test.html')

app.run(host='0.0.0.0', port=5000)


