
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="My Python Website")

@app.route("/about")
def about():
    return "<h2>This is the About Page</h2>"

if __name__ == "__main__":
    app.run(debug=True)
