import module
import http.server
from flask import Flask, render_template
from flask import request
  
app = Flask(__name__, template_folder="template")

@app.route('/register', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # debug in console
    print(request.form.values)
    print(request.form.get('payment', 'Not set'))
    # send back to client
    return 'The /register app.route works!' 

app.run(host='0.0.0.0', port=8080)

