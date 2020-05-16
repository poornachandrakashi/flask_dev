#Learning Flask application.

from flask import Flask

app=Flask(__name__)

@app.route("/")   #Empty url
def index():
    return "HEllo,world!!!"

@app.route("/<string:name>")
def hello(name):
    name=name.capitalize()
    return f"<h1>Hello {name}!</h1>"




if __name__=='__main__':
    app.run(debug=True)
