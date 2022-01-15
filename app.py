#Entry-Point for Application

from flask import Flask, render_template
from flask_restful import Api
from db import db
from resources.employee import Employee, Employees


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "hahahahah"
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()
    
@app.route('/', methods=['GET'])
def home():

    return render_template("index.html")

    

api.add_resource(Employee, '/employee/<string:param>')
api.add_resource(Employees, '/employees')

    
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, host='0.0.0.0', debug=True)
