from flask import Flask
import os

os.environ['FLASK_DEBUG'] = '1'
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome"

# $env:FLASK_ENV="development" (for auto reload at time of save)

@app.route("/about")
def about():
    return "Hii I'm Gautam Singh"

from controller import *

# if __name__ == ('__main__'):
#     app.run(debug=True)