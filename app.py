import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'flask_cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:cookbook33@ds233320.mlab.com:33320/flask_cookbook'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           countries=mongo.db.countries.find(),
                           courses=mongo.db.courses.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
