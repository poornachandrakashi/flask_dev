#Learning Flask application.
#Rendering template
from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")   #Empty url
def index():
    headline="Aishwarya"
    return render_template("index.html",headline=headline)

@app.route("/<string:name>")
def hello(name):
    name=name.capitalize()
    return  render_template("index.html",name=name)

@app.route("/bye")
def bye():
    headline="goodbye"
    return render_template("index.html",headline=headline)



if __name__=='__main__':
    app.run(debug=True)
