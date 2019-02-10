import os
from flask import Flask, render_template, redirect, request, url_for, session, flash, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)
# Set app.configs
app.config["MONGO_DBNAME"] = 'flask_cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:cookbook33@ds233320.mlab.com:33320/flask_cookbook'

# Set app variables
mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
# route to index page
def index():
    if 'username' in session:
        return redirect(url_for('get_recipes'))
    return render_template('index.html')


@app.route('/logged_in')
# When user is verified as logged in redirect to the courses page
def logged_in():
    return redirect(url_for('courses'))


@app.route('/login', methods=['POST'])
# route to and logic for the login page
def login():
    users = mongo.db.users
    login_user = users.find_one({'user_name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('courses'))
    # flash error message
    flash("An invalid Username/Password combination has been entered. Please try again.")
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
# route to and logic for the registration page
def register():
    if request.method == 'POST':
        users = mongo.db.users
        current_user = users.find_one({'user_name': request.form['username']})

        if current_user is None:
            hashpass = bcrypt.hashpw(
                request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one(
                {'user_name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('courses'))

    # flash error message
    flash("That Username already exists. Please choose another one.")
    return render_template('index.html')


@app.route('/logout')
def logout():
    # remove user from the session and return to index page
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/get_recipes')
# route to and logic for the recipe page, returns recipes by newest
def get_recipes():
    recipes = mongo.db.recipes.find().sort([['_id', -1]])
    return render_template("recipes.html",
                           recipes=recipes)


@app.route('/add_recipe')
# route to and logic for the add_recipe page
def add_recipe():
    countries = mongo.db.countries.find()
    courses = mongo.db.courses.find()
    return render_template('addrecipe.html',
                           countries=countries,
                           courses=courses)


@app.route('/insert_recipe', methods=['POST'])
# function to add a recipe to the recipes collection in the mongo database
def insert_recipe():
    username = session['username']
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('my_page', username=username))


@app.route('/edit_recipe/<recipe_id>')
# function to edit a recipe from the edit recipe page
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_countries = mongo.db.countries.find()
    all_courses = mongo.db.courses.find()
    return render_template('editrecipe.html', recipe=the_recipe, countries=all_countries, courses=all_courses)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
# function to update a recipe in the recipes collection in the mongo database
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
        'tags': request.form.get('tags'),
        'recipe_creator': request.form.get('recipe_creator'),
        'img_url': request.form('img_url')
    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
# function to delete a recipe
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


@app.route('/courses')
# route to and logic for the courses page
def courses():
    recipes = mongo.db.recipes.find()
    return render_template("courses.html",
                           recipes=recipes)


@app.route('/recipes_by_course/<course_type>')
# route to and logic for the recipes_by_course page
def recipes_by_course(course_type):
    courses = mongo.db.courses.find()
    recipes = mongo.db.recipes.find(
        {"course_type": course_type}).sort([['_id', -1]])
    return render_template(
        "recipes_by_course.html",
        courses=courses,
        recipes=recipes)


@app.route('/countries')
# route to and logic for the countries page
def countries():
    recipes = mongo.db.recipes.find()
    return render_template("countries.html",
                           recipes=recipes)


@app.route('/recipes_by_country/<country_name>')
# route to and logic for the recipes_by_country page
def recipes_by_country(country_name):
    countries = mongo.db.countries.find()
    recipes = mongo.db.recipes.find(
        {"country_name": country_name}).sort([['_id', -1]])
    return render_template(
        "recipes_by_country.html",
        countries=countries,
        recipes=recipes)


@app.route('/my_page/<username>')
# route to and logic for the users personal page
def my_page(username):
    username = session['username']
    get_user = mongo.db.users.find_one({"username": username})
    get_recipes = mongo.db.recipes.find(
        {"username": username}).sort([['_id', -1]])
    return render_template('my_page.html', username=username, users=get_user, recipes=get_recipes)


@app.route('/my_recipe/<recipe_id>')
# route to and logic for the my_recipe page
def my_recipe(recipe_id):
    my_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_countries = mongo.db.countries.find()
    all_courses = mongo.db.courses.find()
    return render_template('my_recipe.html', recipe=my_recipe, countries=all_countries, courses=all_courses)


@app.route('/delete_my_recipe/<recipe_id>')
# function to delete a recipe from the my_recipe page, and return user to the my_page
def delete_my_recipe(recipe_id):
    username = session['username']
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('my_page', username=username))


@app.route('/insert_my_recipe', methods=['POST'])
# function to add a recipe to the recipes collection in the mongo database, from the my_recipe page, and then return user to the my_page
def insert_my_recipe():
    username = session['username']
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('my_page', username=username))


@app.route('/about')
# route to the about page
def about():
    return render_template('about.html')


@app.route('/full_page_view/<recipe_id>')
# route to the full view page
def full_page_view(recipe_id):
    view_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_countries = mongo.db.countries.find()
    all_courses = mongo.db.courses.find()
    return render_template('full_page_view.html', recipe=view_recipe, countries=all_countries, courses=all_courses)


if __name__ == '__main__':
    app.secret_key = 'ssssshhhhh'
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=False)
