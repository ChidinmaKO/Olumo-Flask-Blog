from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "World Class Research Engineers")
    return f'<h1>Home Page for {escape(name)}!</h1>'

@app.route('/about')
def about():
    return f'<h2>About Page!</h2>'

if __name__ == '__main__':
    app.run(debug=True)