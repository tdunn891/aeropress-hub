import os
import json
import re
import time
import datetime
from flask import Flask, render_template, redirect, request, url_for, jsonify
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


@app.route('/')
@app.route('/index')
def index():
    # Renders index.html
    return render_template('index.html',
                           get_brews_active='active',
                           title="Brew Browser")


@app.route('/get_brews')
def get_brews():
    # Retreives filtered, sorted brews from MongoDB, and returns jsonified rendered template: response.html

    # serialised filters for current page
    serial_filters = str(request.query_string)[2:-1]
    # print(request.args)

    # if all arguments are populated, save arguments as list
    if all(arg in request.args for arg in ('brew_source', 'brewer', 'filter')):
        brew_source_args = request.args.getlist('brew_source')
        brewer_args = request.args.getlist('brewer')
        filter_args = request.args.getlist('filter')
    else:
        # no matching records
        return jsonify({'data': '<h6>No Matching Records</h6>'})

    # Pagination limit: 8 results per page
    limit = 8

    if 'offset' in request.args:
        # get offset from query string
        offset = int(request.args['offset'])
        # remove first 2 parameters from serial_filters (limit and offset)
        serial_filters = serial_filters.split('&', 2)[2]
        # print('SERIAL_FILTERS_2: ' + str(serial_filters))
    else:
        # if offset not provided, offset: 0
        offset = 0

    # if sort-by in query string
    if 'sort-by' in request.args:
        # get sort_field from request argument
        sort_field = str(request.args['sort-by'])
    else:
        # sort by barista
        sort_field = "barista"

    # if sort field is Most Popular, Coffee Grind, or Year, sort descending
    if sort_field in ['likes', 'details.coffee_dose_g', 'year']:
        sort_direction = -1
        mongo_sort_operator = "$lte"
    else:
        # sort ascending
        sort_direction = 1
        mongo_sort_operator = "$gte"

    # all brews
    brew = mongo.db.brews

    # filtered and sorted records
    starting_id = brew.find({
        "brew_source": {"$in": brew_source_args},
        "details.brewer": {"$in": brewer_args},
        "details.filter": {"$in": filter_args}
    }).collation({"locale": "en"}).sort([(sort_field, sort_direction), ('_id', sort_direction)])

    # select only records to be displayed on current page
    brews = starting_id[offset:offset+limit]
    # count of filtered records
    filtered_records_count = str(starting_id.count())
    brews_displayed = brews.count(with_limit_and_skip=True)

    # next url for right chevron anchor
    next_url = '/get_brews?limit=' + \
        str(limit) + '&offset=' + str(offset + limit) + '&' + serial_filters
    # prev url for left chevron anchor
    prev_url = '/get_brews?limit=' + \
        str(limit) + '&offset=' + str(offset - limit) + '&' + serial_filters

    # number of pages required, and extra records
    num_pages, extra_records = divmod(int(filtered_records_count), limit)

    # if extra_records exist, an additional page is required
    if extra_records > 0:
        num_pages += 1

    # current page, used as input to calculate which records are displayed
    current_page = ((int(offset)+1) // limit) + 1

    # prepare  pagination urls for each page number
    urls = {}
    for page_number in range(1, num_pages+1):
        offset_2 = limit * (page_number - 2)
        urls[page_number] = '/get_brews?limit=' + \
            str(limit) + '&offset=' + \
            str(offset_2 + limit) + '&' + serial_filters

    # count of total records
    total_records = mongo.db.brews.count()

    return jsonify({'data': render_template('response.html',
                                            brews=brews,
                                            total_records=total_records,
                                            filtered_records_count=filtered_records_count,
                                            num_pages=num_pages,
                                            urls=urls,
                                            prev_url=prev_url,
                                            next_url=next_url,
                                            offset=offset,
                                            brews_displayed=brews_displayed,
                                            current_page=current_page)})
# winner filters
#     rgx = re.compile('Winner.', re.IGNORECASE)
#     winners_only = mongo.db.brews.find({"brew_name": rgx})


@app.route('/add_brew')
def add_brew():
    # renders Add Brew page, ready for user form input
    return render_template("add_brew.html",
                           add_brew_active="active",
                           title="Add Brew")


@app.route('/insert_brew', methods=['GET', 'POST'])
def insert_brew():
    # inserts record into database

    brews = mongo.db.brews
    if request.method == 'POST':
        req = request.form
        record = {
            "brew_name": req.get("brew_name"),
            "year": datetime.datetime.now().year,
            "place": 100,
            "barista": req.get("barista_name"),
            "country": req.get("country"),
            "brew_source": "Average Joe",
            "total_brew_time": int(req.get("brew_time")),
            "steps": req.get("steps-text-area").split('\r\n'),
            "details": {
                "coffee_dose_g": int(req.get("coffee_weight")),
                "grind": int(req.get("grind_size")),
                "water_temp_c": int(req.get("water_temp")),
                "brewer": req.get("brewer"),
                "filter": req.get("filter")
            },
            "likes": 0
        }
    brews.insert_one(record)
    return redirect(url_for('index'))


@app.route('/edit_brew/<brew_id>')
def edit_brew(brew_id):
    # renders Edit Brew page, presenting user with form input
    # find user-selected brew, so that it is ready for editing
    brew = mongo.db.brews.find_one({'_id': ObjectId(brew_id)})

    return render_template('edit_brew.html',
                           brew=brew,
                           brewers=['Upright', 'Inverted'],
                           filters=['Paper', 'Paper x2',
                                    'Metal', 'Metal \u002B Paper'],
                           title="Edit Brew")


@app.route('/update_brew/<brew_id>', methods=['GET', 'POST'])
def update_brew(brew_id):
    # posts updates from Edit Brew page to database
    if request.method == 'POST':
        req = request.form
        mongo.db.brews.find_one_and_update(
            {'_id': ObjectId(brew_id)},
            {'$set': {
                'brew_name': req.get('brew_name'),
                "brew_name": req.get("brew_name"),
                "barista": req.get("barista_name"),
                "country": req.get("country"),
                "total_brew_time": int(req.get("brew_time")),
                "steps": req.get("steps-text-area").split('\r\n'),
                "details": {
                    "coffee_dose_g": int(req.get("coffee_weight")),
                    "grind": int(req.get("grind_size")),
                    "water_temp_c": int(req.get("water_temp")),
                    "brewer": req.get("brewer"),
                    "filter": req.get("filter")
                }
            }})
        return redirect(url_for('index'))


@app.route('/increase_likes/<brew_id>', methods=['GET', 'POST'])
def increase_likes(brew_id):
    # increases like count by 1
    mongo.db.brews.find_one_and_update(
        {'_id': ObjectId(brew_id)},
        {'$inc': {'likes': 1}}
    )
    return redirect(url_for('index'))


@app.route('/delete_brew/<brew_id>')
def delete_brew(brew_id):
    # deletes brew from database
    mongo.db.brews.remove({'_id': ObjectId(brew_id)})
    return redirect(url_for('index'))

# testing purposes only (EMPTY)
# TODO: remove empty db option
@app.route('/empty_db')
def empty_db():
    mongo.db.brews.remove({})
    return redirect(url_for('index'))


@app.route('/about')
def about():
    # renders About page
    return render_template('about.html',
                           about_active='active',
                           title="About")


@app.errorhandler(404)
def error404(notfound):
    # Renders ERROR 404 page
    return render_template('error404.html',
                           title="404 - Page Not Found")


if __name__ == '__main__':
    # app.run(host=os.environ.get('IP'),
            # port=int(os.environ.get('PORT')),
            # debug=True)
    app.run(host=IP,
            port=int(PORT),
            debug=True)
