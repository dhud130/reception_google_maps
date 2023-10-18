from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("template.html", var = 123, tes = "\n testing test")

if __name__ == '__main__':
    app.run()