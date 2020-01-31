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
    return render_template('index.html', get_brews_active='active')


@app.route('/get_brews')
def get_brews():
    total_records = mongo.db.brews.count()
    # * below is serial of filters for current page, so eg 'next url' will need different offset'
    serial_filters = str(request.query_string)[2:-1]

    if 'brew_source' in request.args:
        brew_source_array = request.args.getlist('brew_source')
    else:
        return jsonify({'data': '<h6>No Matching Records</h6>'})

    if 'brewer' in request.args:
        brewer_array = request.args.getlist('brewer')
    else:
        return jsonify({'data': '<h6>No Matching Records</h6>'})

    if 'filter' in request.args:
        filter_array = request.args.getlist('filter')
    else:
        return jsonify({'data': '<h6>No Matching Records</h6>'})

    brew = mongo.db.brews

    # Pagination
    #    https://www.youtube.com/watch?v=Lnt6JqtzM7I
    # * which ever number is clicked, the offset would be Number * Limit
    limit = 8
    # * default offset should be 0 (shows first page)
    if 'offset' in request.args:
        offset = int(request.args['offset'])
        # * remove first 2 parameter from serial_filters (limit and offset)
        serial_filters = serial_filters.split('&', 2)[2]
        print('SERIAL_FILTERS_2: ' + str(serial_filters))
    else:
        offset = 0

    # * offset = limit * (page number - 1)
    if 'sort-by' in request.args:
        sort_field = str(request.args['sort-by'])
    else:
        sort_field = "barista"

    # if Most Popular or Coffee Grind, sort descending
    if sort_field in ['likes', 'details.coffee', 'year']:
        sort_direction = -1
        mongo_sort_operator = "$lte"
    else:
        # else sort ascending
        sort_direction = 1
        mongo_sort_operator = "$gte"

    # * this is just maintaining the full sorted records each time (by field, then by id)
    starting_id = brew.find({
        "brew_source": {"$in": brew_source_array},
        "details.brewer": {"$in": brewer_array},
        "details.filter": {"$in": filter_array}
    }).collation({"locale": "en"}).sort([(sort_field, sort_direction), ('_id', sort_direction)])

    brews = starting_id[offset:offset+limit]
    filtered_records_count = str(starting_id.count())
    brews_displayed = brews.count(with_limit_and_skip=True)

    # ? next and prev prb shouldn be required, just get from urls dict
    # * the first 2 terms are right, need to exclude offset and limit from serial_filters, before passing in
    next_url = '/get_brews?limit=' + \
        str(limit) + '&offset=' + str(offset + limit) + '&' + serial_filters
    prev_url = '/get_brews?limit=' + \
        str(limit) + '&offset=' + str(offset - limit) + '&' + serial_filters

    # calculate number of pages required
    num_pages, overflow = divmod(int(filtered_records_count), limit)
    current_page = ((int(offset)+1) // limit) + 1

    # if there's an overflow, increase num_pagese by 1
    if overflow > 0:
        num_pages += 1

    # prepare urls for each page number
    urls = {}
    for page_number in range(1, num_pages+1):
        offset_2 = limit * (page_number - 2)
        urls[page_number] = '/get_brews?limit=' + \
            str(limit) + '&offset=' + \
            str(offset_2 + limit) + '&' + serial_filters

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
    return render_template("add_brew.html", add_brew_active="active")


@app.route('/insert_brew', methods=['GET', 'POST'])
def insert_brew():
    brews = mongo.db.brews
    if request.method == 'POST':
        req = request.form
        stepsArray = req.get("steps-text-area").split('\r\n')
        # convert total seconds to mins and seconds
        total_seconds = int(req.get("brew_time"))
        m, s = divmod(total_seconds, 60)
        formatted_time = f'{m:01d}:{s:02d}'

        payload = {
            "brew_name": req.get("brew_name"),
            "year": datetime.datetime.now().year,
            "place": 100,
            "barista": req.get("barista_name"),
            "country": req.get("country"),
            "brew_source": "Average Joe",
            "total_brew_time": formatted_time,
            "steps": stepsArray,
            "details": {
                # TODO: remove 'g' and 'C'
                "coffee": req.get("coffee_weight") + "g",
                "grind": int(req.get("grind_size")),
                "water": req.get("water_temp") + "\u00b0C",
                "brewer": req.get("brewer"),
                "filter": req.get("filter")
            },
            "likes": 0
        }
    brews.insert_one(payload)
    return redirect(url_for('index'))


@app.route('/edit_brew/<brew_id>')
def edit_brew(brew_id):
    brew = mongo.db.brews.find_one({'_id': ObjectId(brew_id)})
    # convert mins/secs to total secs
    mins = brew['total_brew_time'][0]
    secs = brew['total_brew_time'][2:]
    total_secs = int(mins)*60 + int(secs)
    # print(total_secs)
    prefilled_filter = brew['details']['filter']
    # print(prefilled_filter)
    filter_dict = {
        "Paper": '',
        "Paper x2": '',
        "Metal": '',
        "Metal \u002B Paper": ''
    }

    for i in filter_dict:
        if (i == prefilled_filter):
            filter_dict[prefilled_filter] = "selected='selected'"

    return render_template('edit_brew.html',
                           brew=brew,
                           total_brew_time=total_secs,
                           filter_dict=filter_dict)


@app.route('/update_brew/<brew_id>', methods=['GET', 'POST'])
def update_brew(brew_id):
    if request.method == 'POST':
        req = request.form
        # convert total seconds to mins and seconds
        total_seconds = int(req.get("brew_time"))
        m, s = divmod(total_seconds, 60)
        formatted_time = f'{m:01d}:{s:02d}'
        # populate list from steps
        stepsArray = req.get("steps-text-area").split('\r\n')
        mongo.db.brews.find_one_and_update(
            {'_id': ObjectId(brew_id)},
            {'$set': {
                'brew_name': req.get('brew_name'),
                "brew_name": req.get("brew_name"),
                "barista": req.get("barista_name"),
                "country": req.get("country"),
                "total_brew_time": formatted_time,
                "steps": stepsArray,
                "details": {
                    # TODO: remove 'g' and 'C'
                    "coffee": req.get("coffee_weight") + "g",
                    "grind": int(req.get("grind_size")),
                    "water": req.get("water_temp") + "\u00b0C",
                    "brewer": req.get("brewer"),
                    "filter": req.get("filter")
                }
            }})
        return redirect(url_for('index'))


@app.route('/increase_likes/<brew_id>', methods=['GET', 'POST'])
def increase_likes(brew_id):
    mongo.db.brews.find_one_and_update(
        {'_id': ObjectId(brew_id)},
        {'$inc': {'likes': 1}}
    )
    return redirect(url_for('index'))


@app.route('/delete_brew/<brew_id>')
def delete_brew(brew_id):
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
    return render_template('about.html', about_active='active')


@app.errorhandler(404)
def error404():
    return render_template('error404.html')


if __name__ == '__main__':
    # app.run(host=os.environ.get('IP'),
            # port=int(os.environ.get('PORT')),
            # debug=True)
    app.run(host=IP,
            port=int(PORT),
            debug=True)
