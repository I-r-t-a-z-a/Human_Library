# app.py
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Test Text"         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app

    # app.py: the entry and exit point to our application. application layer
    # service.py: converst the request into a response. business logic
    # models.py: handles everything involving database. data
    # MVC: Model View Controller Pattern