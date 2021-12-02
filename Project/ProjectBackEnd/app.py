from flask import Flask,render_template


app=Flask(__name__)

@app.route('/')
def index():
    count = 19
    return render_template('index.html',count=count)


# @app.route('/about')
# def about():

#     return render_template('about.html')

# @app.route('/programs')
# def programs():

#     return render_template('programs.html')

if __name__=='__main__':
    app.run(debug=True)