from flask import Flask,render_template
import datetime

app=Flask(__name__)

@app.route('/')
def index():
    now=datetime.datetime.now()
    new_year=now.month==1 and now.day==1
    return render_template("index.html",new_year=new_year)

if __name__=='__main__':
    app.run(debug=True)