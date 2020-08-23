from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/catalog')
def catalog():
    return render_template("catalog.html")


@app.route('/catalog_pvc')
def catalog_pvc():
    return render_template("catalog_pvc.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html")


if __name__ == '__main__':
    app.run(debug=True)
