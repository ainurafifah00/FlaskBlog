from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
	app.run(debug=True)