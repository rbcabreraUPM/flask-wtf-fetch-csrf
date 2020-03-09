from flask import Flask, render_template,request, jsonify
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'  
app.config['SESSION_COOKIE_SECURE'] = False  
csrf = CSRFProtect(app)

@csrf.error_handler
def csrf_error(reason):
	print(reason)
	return render_template('csrf_error.html', reason=reason), 400

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/post',  methods=['POST'])
def test_Csrf():
	print("GG")
	return jsonify([]),200

if __name__ == '__main__':
   app.run(debug=True)