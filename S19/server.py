from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)


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