import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'flask_cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:cookbook33@ds233320.mlab.com:33320/flask_cookbook'

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           recipes=mongo.db.recipes.find())


@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           countries=mongo.db.countries.find(),
                           courses=mongo.db.courses.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_countries = mongo.db.countries.find()
    all_courses = mongo.db.courses.find()
   #  user = mongo.db.recipes.find()
    return render_template('editrecipe.html', recipe=the_recipe, countries=all_countries, courses=all_courses)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.updateOne({'_id': ObjectId(recipe_id)},
                      {
        'country_name': request.form.get('country_name'),
        'course_type': request.form.get('course_type'),
        'recipe_name': request.form.get('recipe_name'),
        'user_name': request.form.get('user_name'),
        'recipe_description': request.form.get('recipe_description'),
        'preparation_time': request.form.get('preparation_time'),
        'cooking_time': request.form.get('cooking_time'),
        'total_time': request.form.get('total_time'),
        'servings': request.form.get('servings'),
        'ingredients': request.form.get('ingredients'),
        'instructions': request.form.get('instructions'),
        'allergens': request.form.get('allergens'),
        'tags': request.form.get('tags')
    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


@app.route('/courses')
def courses():
    return render_template("courses.html",
                           recipes=mongo.db.recipes.find())


@app.route('/recipes_by_course/<course_type>')
def recipes_by_course(course_type):
    return render_template(
        "recipes_by_course.html",
        recipes=mongo.db.recipes.find({"course_type": course_type}),
        courses=mongo.db.courses.find()
    )


@app.route('/countries')
def countries():
    return render_template("countries.html",
                           recipes=mongo.db.recipes.find())


@app.route('/recipes_by_country/<country_name>')
def recipes_by_country(country_name):
    return render_template(
        "recipes_by_country.html",
        recipes=mongo.db.recipes.find({"country_name": country_name}),
        countries=mongo.db.countries.find()
    )


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
