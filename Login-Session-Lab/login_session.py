from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

login_session = {'quote':'','author':'','age':''}

@app.route('/', methods=["GET","POST"]) # What methods are needed?
def home():
	if request.method == "GET":
		return render_template('home.html')
	else:
		quote=request.form['quote']
		author=request.form['author']
		age=request.form['age']

		try: 
			login_session['quote'] = quote
			login_session['author'] = author
			login_session['age'] = age
			return redirect(url_for('thanks'))
		except:
			print('the key user isn’t in login_session')
			return redirect(url_for('error'))



@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html',login_session=login_session)



@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)