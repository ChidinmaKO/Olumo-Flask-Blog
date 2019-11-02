from flask import render_template, url_for, redirect, flash
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Chidinma Kalu',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'October 20, 2019'
    },
    {
        'author': 'Victoria Olugu',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'October 21, 2019'
    },
    {
        'author': 'Tobiloba Okereke',
        'title': 'Blog Post 3',
        'content': 'Third Post content',
        'date_posted': 'October 25, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'kchidinmavictoria@gmail.com' and form.password.data == 'password':
            flash('Welcome back { form.username.data }! You are now logged in.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)