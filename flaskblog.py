from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

'''
	Token is generated from python secrets.token_hex(16)
'''
app.config['SECRET_KEY'] = '24de8f3a063335c5b874ee082243ac6e'


#dummy database
posts = [
	{
		'author':'Ainur Afifah',
		'title':'Blog Post 1',
		'content':'First post content',
		'date_posted':'Feb 25, 2021'
	},
	{

		'author':'Ainur Amirah',
		'title':'Blog Post 2',
		'content':'First post content',
		'date_posted':'Feb 26, 2021'
	}
]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def registration():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)