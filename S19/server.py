from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return 'Hello, this is a blog about Infrastructure'

@app.route('/blog/2020/dogs')
def blog2():
    return 'Hello,this is the dog blog'

@app.route('/favicon.ico')
def favicon():
    return 'Hello,this is the dog blog'