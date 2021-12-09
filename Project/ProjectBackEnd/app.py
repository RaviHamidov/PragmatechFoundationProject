from flask import Flask

app=Flask(__name__)

from routes.admin.routes import *
from routes.app.routes import *    

if __name__=='__main__':
    app.run(debug=True)