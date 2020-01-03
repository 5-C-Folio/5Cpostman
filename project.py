from flask import Flask, request, redirect, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Car

engine = create_engine('sqlite:///cars.db?check_same_thread=False')
Base.metadata.bind = engine

DBsession = sessionmaker(bind = engine)
session = DBsession()

@app.route('/car/<int:id>')
def get_car(id):
    car = session.query(Car).filter_by(id = id).one()
    return jsonify(Car_result = car.serialize)


@app.route('/car/post', methods = ['GET', 'POST'])
def post_new():
    if request.method == 'POST':
        new_car = Car(model = request.json["model"], color = request.json["color"],
                     year = request.json["year"], license_plate = request.json["license_plate"])
        session.add(new_car)
        session.commit()
        return "201, OK"
        session.commit()
        return "201, OK"

if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)