import os
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


@app.route('/insert_brew', methods=['POST', 'GET'])
def insert_brew():
    # brews = mongo.db.brews
    # brews.insert_one(request.form.to_dict())
    return render_template("insert_brew.html")
    # return redirect(url_for('get_brews'))
    # TODO: correct


if __name__ == '__main__':
    # app.run(host=os.environ.get('IP'),
            # port=int(os.environ.get('PORT')),
            # debug=True)
    app.run(host=IP,
            port=int(PORT),
            debug=True)
