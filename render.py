#Learning Flask application.
#Rendering template
from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")   #Empty url
def index():
    return render_template("index.html")

@app.route('/oxford')
def oxford():
    return render_template("oxford.html")





if __name__=='__main__':
    app.run(debug=True)
