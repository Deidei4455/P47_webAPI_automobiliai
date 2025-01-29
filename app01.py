from serializers import CarsSchema
from models import db, Automobil
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def cars_api():
    all_cars = Automobil.query.all()
    cars_data = [CarsSchema.model_validate(car).model_dump() for car in all_cars]
    return jsonify(cars_data)


@app.route("/frontend", methods=["GET", "POST"])
def frontend():
    all_cars = Automobil.query.all()
    cars_data = [CarsSchema.model_validate(car).model_dump() for car in all_cars]
    return render_template("cars.html", cars=cars_data)


if __name__ == "__main__":
    app.run()
