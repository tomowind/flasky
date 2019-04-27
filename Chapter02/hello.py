from flask import Flask, request, make_response, redirect, abort
app = Flask(__name__)

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
	if name != 'sangmin':
		abort(404)
	return f'<h1>Hello, {name}!</h1>'

@app.route('/agent')
def user_agent():
	user_agent = request.headers.get('User-Agent')
	return f'<p>Your browser is {user_agent}'

@app.route('/bad')
def bad_request():
	return '<h1>Bad Request</h1>', 400

@app.route('/cookie')
def cookie():
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response

@app.route('/redirect')
def red():
	return redirect('https://github.com/tomowind/')