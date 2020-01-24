import os
import json
import re
import time
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
    return render_template('index.html')


@app.route('/get_brews')
def get_brews():
    total_records = mongo.db.brews.count()
    # brews = mongo.db.brews.find().sort('barista', 1)
    print('REQUEST.URL: ' + str(request.url))
    serial_filters = str(request.query_string)[2:-1]
    print('serial_filters: ' + serial_filters)

# * Add all filtering here, so brew has been filtered -----------------------
# * by default, if no filters in request.args, don't apply filters
# * if any arrays are empty, render blank
# TODO: FIX: if cursor is blank, it errors when it should show blank (eg turn off Champ)

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

    filtered_records = mongo.db.brews.find({
        "brew_source": {"$in": brew_source_array},
        "details.brewer": {"$in": brewer_array},
        "details.filter": {"$in": filter_array}
    })

# * ----------------------------------------------

    brew = mongo.db.brews

    # Pagination
    #    https://www.youtube.com/watch?v=Lnt6JqtzM7I
    # TODO: set offset limits
    # * which ever number is clicked, the offset would be Number * Limit
    limit = 5
    # * default offset should be 0 (shows first page)
    if 'offset' in request.args:
        offset = int(request.args['offset'])
        print('OFFSET provided: ' + str(offset))
    else:
        offset = 0
        print('DEFAULT OFFSET: ' + str(offset))

    # * offset = limit * (page number - 1)
    # * so for first page: offset = 5 * (1-1) = 0
    # * second page: offset = 5 * (2-1) = 5
    # * third page: offset = 5 * (3-1) = 10

    # * the sort field would have to be dynamic (in apply_filters especially). the order by also needs to be dynamic
    if 'sort-by' in request.args:
        sort_field = str(request.args['sort-by'])
        print('sort_field in args: ' + sort_field)
    else:
        print('NOT sort_field in args')
        # * use fallback sort, _id
        sort_field = "_id"

    # if Most Popular or Coffee Grind, sort descending
    if sort_field in ['likes', 'details.coffee']:
        sort_direction = -1
        mongo_sort_operator = "$lte"
    else:
        # else sort ascending
        sort_direction = 1
        mongo_sort_operator = "$gte"

    starting_id = brew.find({
        "brew_source": {"$in": brew_source_array},
        "details.brewer": {"$in": brewer_array},
        "details.filter": {"$in": filter_array}
    }).sort(sort_field, sort_direction)

    if '.' in sort_field:
        sort_field_split = sort_field.split('.')
        print('sortfield1: ', sort_field_split[0])
        print('sortfield2: ', sort_field_split[1])
        last_id = starting_id[offset][sort_field_split[0]][sort_field_split[1]]
        print('split required')
    else:
        print('NO split required')
        last_id = starting_id[offset][sort_field]

    brews = brew.find({sort_field: {mongo_sort_operator: last_id},
                       "brew_source": {"$in": brew_source_array},
                       "details.brewer": {"$in": brewer_array},
                       "details.filter": {"$in": filter_array}
                       }).sort(
        sort_field, sort_direction).limit(limit)
    print('TOTAL RECORDS: ' + str(total_records))
    filtered_records_count = str(starting_id.count())
    print('FILTERED RECORDS COUNT: ' + filtered_records_count)
    paginated_brews_displayed = brews.count(with_limit_and_skip=True)
    print('PAGINATED_BREWS_DISPLAYED: ' + str(paginated_brews_displayed))

    # TODO: showing (x of y) from z (Unfiltered: W)
    # ? next and prev prb shouldn be required, just get from urls dict
    next_url = '/get_brews?limit=' + \
        str(limit) + '&offset=' + str(offset + limit) + '&' + serial_filters
    prev_url = '/get_brews?limit=' + \
        str(limit) + '&offset=' + str(offset - limit) + '&' + serial_filters

    # * could rename num_pages to full_pages (so numpages doesn't mutate)
    num_pages, overflow = divmod(int(filtered_records_count), limit)
    print('numpages: ' + str(num_pages))
    print('overflow: ' + str(overflow))

    # * if there's an overflow, we need another page
    if overflow > 0:
        num_pages += 1

    # * needs to prepare urls for each number
    urls = {}
    for page_number in range(1, num_pages+1):
        offset_2 = limit * (page_number - 2)
        urls[page_number] = '/get_brews?limit=' + \
            str(limit) + '&offset=' + \
            str(offset_2 + limit) + '&' + serial_filters
        print('Page num: ' + str(page_number))
        print('url: ' + str(urls[page_number]))

    return jsonify({'data': render_template('response.html',
                                            brews=brews,
                                            total_records=total_records,
                                            filtered_records_count=filtered_records_count,
                                            num_pages=num_pages,
                                            urls=urls,
                                            prev_url=prev_url,
                                            next_url=next_url)})

    # return render_template("get_brews.html",
    #                        brews=brews,
    #                        total_records=total_records,
    #                        filtered_records_count=total_records,
    #                        num_pages=num_pages,
    #                        urls=urls,
    #                        prev_url=prev_url,
    #                        next_url=next_url)

# winner filters
#     rgx = re.compile('Winner.', re.IGNORECASE)
#     winners_only = mongo.db.brews.find({"brew_name": rgx})


# ? make this async
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

    # * test, won't work bc don't have access to the urls here

    # sort
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

        # TODO: Remove units from database
        payload = {
            "brew_name": req.get("brew_name"),
            "barista": req.get("barista_name"),
            "brew_source": "Average Joe",
            "steps": stepsArray,
            "total_brew_time": formatted_time,
            "details": {
                "coffee": req.get("coffee_weight") + "g",
                "grind": int(req.get("grind_size")),
                "water": req.get("water_temp") + "\u00b0C",
                "brewer": req.get("brewer"),
                "filter": req.get("filter")
            },
            "likes": 1
        }
    brews.insert_one(payload)
    # * Could try to AJAX this
    return redirect(url_for('index'))


@app.route('/update_brew/<brew_id>', methods=['GET', 'POST'])
def update_brew(brew_id):
    if request.method == 'POST':
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


@app.route('/delete_brew/<brew_id>')
def delete_brew(brew_id):
    mongo.db.brews.remove({'_id': ObjectId(brew_id)})
    # TODO: replace sleep
    time.sleep(0.5)
    return redirect(url_for('get_brews'))

# testing purposes only (EMPTY)
@app.route('/empty_db')
def empty_db():
    mongo.db.brews.remove({})
    return redirect(url_for('get_brews'))


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    # app.run(host=os.environ.get('IP'),
            # port=int(os.environ.get('PORT')),
            # debug=True)
    app.run(host=IP,
            port=int(PORT),
            debug=True)
