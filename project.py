from flask import Flask, request, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Car

engine = create_engine('sqlite:///cars.db?check_same_thread=False')
Base.metadata.bind = engine

DBsession = sessionmaker(bind = engine)
session = DBsession()

@app.route('/car/<int:id>', methods = ['GET','PUT'])
def get_car(id):
    #get a single record by id
    if request.method == 'GET':
        car = session.query(Car).filter_by(id = id).one()
        return jsonify(Car_result = car.serialize)
    if request.method == 'PUT':
        #update a single record by id
        car = session.query(Car).filter_by(id=id).one()
        #an inelegant solution until I figure out something better
        for key, values in request.json.items():
            if key == "model":
                car.model = values
            if key == "color":
                car.color = values
            if key == "year":
                car.year = values
            if key == "license_plate":
                car.license_plate = values
        session.add(car)
        session.commit()
        #return updated record
        return jsonify(car = car.serialize)



@app.route('/car/post', methods = ['POST'])
def post_new():
    #create new record
    if request.method == 'POST':
        new_car = Car(model = request.json["model"], color = request.json["color"],
                     year = request.json["year"], license_plate = request.json["license_plate"])
        session.add(new_car)
        session.commit()
        #it would be nice to return the new record, but easier to return all?
        return "201, OK"


if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)