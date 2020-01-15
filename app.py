import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

IP = "127.0.0.1"
PORT = "5500"

MONGO_URI = "mongodb+srv://root:ypb3Sgz1@myfirstcluster-bgxgx.mongodb.net/aeropress?retryWrites=true&w=majority"

app.config["MONGO_DBNAME"] = 'aeropress'
# app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config["MONGO_URI"] = MONGO_URI

mongo = PyMongo(app)
# print(mongo)


@app.route('/')
@app.route('/get_brews')
def get_brews():
    # print(mongo.db.brews.find())
    return render_template("get_brews.html",
                           brews=mongo.db.brews.find())


@app.route('/add_brew')
def add_brew():
    return render_template("add_brew.html")


@app.route('/insert_brew', methods=['GET', 'POST'])
def insert_brew():
    brews = mongo.db.brews
    if request.method == 'POST':
        req = request.form
        # Get in right structure
        # Prepare payload
        payload = {
            "brew_id": 100,
            "brew_name": req.get("brew_name"),
            "barista": req.get("barista_name"),
            "brew_source": "World AeroPress Champion Finalist",
            # TODO: deal with steps
            "steps": [
                "Test step 1",
                "Test step 2"
            ],
            # TODO: convert secs to minutes
            "total_brew_time": req.get("brew_time") + "s",
            "details": {
                "coffee": req.get("coffee_weight") + "g",
                "grind": req.get("grind_size") + "/10",
                "water": req.get("water_temp") + " C",
                "brewer": req.get("brewer"),
                "filter": req.get("filter")
            },
            "notes": req.get("notes"),
            "likes": "",
            # TODO: deal with img_url, or remove
            "img_url": ""
        }
        # print(request.json)
    brews.insert_one(payload)
    return redirect(url_for('get_brews'))

# TODO: test delete
@app.route('/delete_brew/<brew_id>')
def delete_brew():
    brews = mongo.db.brews
    brews.remove()({'id_': ObjectId(brew_id)})
    return redirect(url_for('get_brews'))


if __name__ == '__main__':
    # app.run(host=os.environ.get('IP'),
            # port=int(os.environ.get('PORT')),
            # debug=True)
    app.run(host=IP,
            port=int(PORT),
            debug=True)
