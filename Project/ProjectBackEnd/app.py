from flask import Flask,render_template
from data import cards

app=Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html',cards=cards)


@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/programs')
def programs():

    return render_template('programs.html')
    
if __name__=='__main__':
    app.run(debug=True)