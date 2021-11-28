from flask import Flask 

app=Flask(__name__)

@app.route('/')
def index():
    return 'This is home page'

@app.route('/about')
def about():
    return 'This is about page'

@app.route('/contact')
def contact():
    return 'This is contact page'

if __name__=='__main__':
    app.run(debug=True)