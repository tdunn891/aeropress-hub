import os
import json
import re
import time
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
    # print(mongo.db.brews.count())
    total_records = mongo.db.brews.count()
    # filtered_records = mongo.db.brews.find({})
    brews = mongo.db.brews.find().sort('barista', 1)
    # split out steps
    return render_template("get_brews.html",
                           #    brews=mongo.db.brews.find().so,
                           brews=brews,
                           total_records=total_records,
                           filtered_records_count=total_records)

# winnder filters
# @app.route('/filter_brews')
# def filter_brews():
#     rgx = re.compile('Winner.', re.IGNORECASE)
#     winners_only = mongo.db.brews.find({"brew_name": rgx})
#     return render_template("get_brews.html",
#                            brews=winners_only)

# test
@app.route('/apply_filters')
def apply_filters():
    # print(request.args.to_dict())
    # query_string = request.query_string
    brew_source_array = request.args.getlist('brew_source')
    brewer_array = request.args.getlist('brewer')
    filter_array = request.args.getlist('filter')
    sort_by = request.args['sort-by']
    print(sort_by)

    filtered_records = mongo.db.brews.find({
        "brew_source": {"$in": brew_source_array},
        "details.brewer": {"$in": brewer_array},
        "details.filter": {"$in": filter_array}
    })

    filtered_records_count = filtered_records.count()
    total_records = mongo.db.brews.count()

    if sort_by == 'details.coffee' or sort_by == 'likes':
        sort_direction = -1
    else:
        sort_direction = 1

    filtered_records.sort(sort_by, sort_direction)

    # sort attempt
    # TODO: how to maintain checkboxes after refresh
    return render_template("get_brews.html",
                           brews=filtered_records,
                           filtered_records_count=filtered_records_count,
                           total_records=total_records)


@app.route('/add_brew')
def add_brew():
    return render_template("add_brew.html")


@app.route('/insert_brew', methods=['GET', 'POST'])
def insert_brew():
    brews = mongo.db.brews
    if request.method == 'POST':
        req = request.form

        # Prepare payload (should this be done in js, not here?)
        stepsArray = []
        for i in range(1, 10):
            # TODO: fix steps array (nones)
            step = req.get("step_" + str(i))
            # If step is not none, append to array
            if step != 'None':
                print('Step added: ' + str(i))
                stepsArray.append(step)
            else:
                print('stopping')
                # last step, exit loop
                break

        # mins to seconds
        total_seconds = int(req.get("brew_time"))
        m, s = divmod(total_seconds, 60)
        formatted_time = f'{m:01d}:{s:02d}'
        # print(mins_and_seconds)

        # TODO: New brew should be placed at top of list (do sorting in app.py)
        payload = {
            "brew_name": req.get("brew_name"),
            "barista": req.get("barista_name"),
            "brew_source": "User",
            "steps": stepsArray,
            "total_brew_time": req.get("brew_time") + "s",
            "total_brew_time": formatted_time,
            "details": {
                "coffee": req.get("coffee_weight") + "g",
                "grind": req.get("grind_size") + "/10",
                "water": req.get("water_temp") + " \u00b0C",
                "brewer": req.get("brewer"),
                "filter": req.get("filter")
            },
            "likes": 0
        }
        # print(request.json)
    brews.insert_one(payload)
    return redirect(url_for('get_brews'))


@app.route('/update_brew/<brew_id>', methods=['GET', 'POST'])
def update_brew(brew_id):
    if request.method == 'POST':
        # print('Brew ID: ' + brew_id)
        # print(request.form)
        # print('Coffee Weight: ' + request.form.get('coffee_weight'))
        mongo.db.brews.find_one_and_update(
            {'_id': ObjectId(brew_id)},
            {'$set':
             {
                 'details.coffee': request.form.get('coffee_weight')+'g'
                 # TODO: add other sliders once happy
             }
             }
        )
        time.sleep(0.5)
        # TODO: don't have to reload the page, bc the data is already displayed
        return redirect(url_for('get_brews'))


@app.route('/increase_likes/<brew_id>', methods=['GET', 'POST'])
def increase_likes(brew_id):
    mongo.db.brews.find_one_and_update(
        {'_id': ObjectId(brew_id)},
        {'$inc': {'likes': 1}}
    )
    time.sleep(0.5)
    return redirect(url_for('get_brews'))


# @app.route('/delete_brew')
@app.route('/delete_brew/<brew_id>')
def delete_brew(brew_id):
    # def delete_brew():
    # mongo.db.brews.remove({})
    mongo.db.brews.remove({'_id': ObjectId(brew_id)})
    # TODO: replace sleep
    time.sleep(0.5)
    return redirect(url_for('get_brews'))

# testing purposes only
@app.route('/empty_db')
def empty_db():
    mongo.db.brews.remove({})
    return redirect(url_for('get_brews'))


if __name__ == '__main__':
    # app.run(host=os.environ.get('IP'),
            # port=int(os.environ.get('PORT')),
            # debug=True)
    app.run(host=IP,
            port=int(PORT),
            debug=True)
