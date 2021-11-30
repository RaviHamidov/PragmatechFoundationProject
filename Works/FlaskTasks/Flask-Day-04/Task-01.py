from flask import Flask,request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        user_name=request.form ['Name']
        user_password=request.form['Password']
        if user_name=="Admin" and user_password=="admin42":
            return about()     

    return  f"""
        <form action="/" method="POST">
        <input type="text" placeholder="Name" id="">
        <input type="password" placeholder="Password" id="">
        <input type="submit" value="Submit"> 
        </form>
    """

@app.route('/about')
def about():
    return f""" <h3>Hello World</h3>"""

if __name__=='__main__':
    app.run(debug=True)