from flask import Flask

app=Flask(__name__)

@app.route("/")   #Empty url
def index():
    return "HEllo,world!!!"


if __name__=='__main__':
    app.run(debug=True)
