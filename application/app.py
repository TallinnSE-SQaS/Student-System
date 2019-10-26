from flask import Flask, render_template

app = Flask(
    __name__.partition('.')[0],
    static_folder='../static')

# would be private in a real life application
app.secret_key = 'a3ws4e6d5rgt7hy8uj9@#ZXE$VTBYw4es5dr6tfgyih'


@app.route("/")
def home():
    return render_template('home.html.j2')
