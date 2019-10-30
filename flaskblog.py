from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)