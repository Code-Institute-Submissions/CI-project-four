# Flask Cookbook 

### Code Institute: Data Centric Development Milestone Project

<a href="https://flask-cookbook.herokuapp.com/" target="_blank"> Click here to view website</a>

*Developer: Mark Wilde*

-------




## Index



1. [Project Instructions](#instructions-from-code-institute)
2. [Cookbook Information](#cookbook-information)
3. [UX](#ux)
    * [Design](#design)
    * [User Stories](#user-stories)
4. [Features](#features)
5. [Technologies](#technologies-used)
6. [Database Schema](#database-schema)
7. [Testing](#testing)
    * [User Stories](#user-stories)
    * [Manual Testing](#manual-testing)
    * [Other](#other)
8. [Deployment](#deployment)
9.  [Installation](#installation)
10. [Credits](#credits)




## Instructions From Code Institute



Guidelines for project development:


- Create a web application that allows users to store and easily access cooking recipes
- Put some effort into designing a database schema based on recipes, and any other related properties and entities.
- Make sure to put some thought into the relationships between them, and use foreign keys to connect these pieces of data.
- Create the backend code and frontend form to allow users to add new recipes to the site. Create the backend code to group and summarize the recipes on the site, based on their attributes such as cuisine or country of origin etc.
Create a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category.
- Create the backend code to retrieve a list of recipes.
- Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions.
- Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages.
- Optionally, you may choose to add basic user registration and authentication to the site.
- You should conduct and document tests to ensure that all of your website’s functionality works well.
- Write a README.md file for your project.
- Use Git & GitHub for version control.
- Deploy the final version of your code to a hosting platform such as Heroku.




## Cookbook Information

- This app is for people who may be interesting in learning more about meat and dairy free Asian cuisine. 
- The Cookbook was created with simplicity and ease of use in mind. Users can add, view, edit and delete their own recipes.
- Users can also view, edit and delete recipes of other users.
- With this in mind it is hoped users will personalize their cookbook, keeping the recipes they like best.





## UX




### Design



- Development of the website adhered to a mobile first approach, it implements a simplistic design with minimal content. 

- The Materialize CSS framework underpins the project and was implemented as per convention. 
  
- Users are asked to register or login before being granted access to the website.

- All pages share the same navbar and footer, though each page has a clear purpose and some unique functionality.
  
- Soft colors were used throughout the website in an attempt to help users feel relaxed. 





### User Stories



Several user stories were considered before development began:

1. "I eat a plant-based diet and would like to visit a website with 100% vegan recipes."
2. "I am interested in veganism and would like to visit a website that has a collection of plant-based recipes."
3. "As a parent I want to encourage my children to eat fruits and vegetables, I would like to visit a website with healthy food options."
4. "I live by myself and want to learn about making wholesome meals at home so I don't just order takeaway."
5. "As a person who wants to improve their cooking skills, I'm looking for new recipes to try."
6. "I currently eat an unhealthy diet and want access to recipes that are good for my health."
7. "I want to be able to store all my favorite recipes online, with minimum fuss."
8. "I want to edit and delete recipes."
9. "I want to encourage my friends to consider eating less meat and dairy, and would like to be able to recommend a good recipe website to them."




## Features



| Page          |                                                                                                                                                                                     Description                                                                                                                                                                                      |
| :------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Index         |                                                                                                                                 This is the landing page. It is a basic page with a background image, and a simple registration form and login form.                                                                                                                                 |
| Asian Cuisine | This page displays a welcome message and three courses cards(starter, Main, Dessert), click on a card to see it's recipe collection. All the recipe cards in the collection will be returned. Users can click on a card to view, edit or delete the recipe. If they choose to edit a recipe it will be stored in there personal collection and can be viewed in the My Recipes page. |
| About         |                                                                                                                                           This page gives a brief description of the website's purpose and provides some navigation tips.                                                                                                                                            |
| My Recipes    |                                                                                                                 This page displays the users collection of created recipes in a list from newest to oldest. Users can also view, edit and delete their recipes here.                                                                                                                 |
| All Recipes   |                                      This page displays all recipes in the Cookbook. Users can click on a recipe card for full instructions on cooking time, ingredients etc. User can also edit or delete any recipe. If they choose to edit a recipe it will be stored in their personal collection and can be viewed in the My Recipes page.                                      |
| By Country    |     This page displays five country collection cards, click on a card to see all recipes in that countries collection. All the recipe cards in the countries collection will be returned. Users can click on a card to view, edit or delete the recipe. If they choose to edit a recipe it will be stored in there personal collection and can be viewed in the My Recipes page.     |
| Logout        |                                                                                                                                                       Users can log out at any time and will be returned to the landing page.                                                                                                                                                        |




## Existing/Future Technologies



- An option for users to upload an image which would display on their recipe card (has since been implemented).
  
- A search bar so that users could search recipes by ingredients.




## Technologies Used

### Code Editor



- [Visual Studio Code](https://code.visualstudio.com)
    - The project was developed using the **Visual Studio Code** code editor.



### Front end



- [HTML](https://www.w3schools.com/html/default.asp)
    - The project uses **HTML** to create the pages.

- [CSS](https://www.w3schools.com/css/default.asp)
    - The project uses **CSS** to style the pages.

- [Materialize CSS Framework](https://materializecss.com/)
    - The project uses **Materialize** for styling and responsive design.

- [Material Icons](https://material.io/tools/icons/?style=baseline)
    - The project uses **Material Icons** icons in it's forms.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** for responsiveness.
  
- [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript)
    - The project uses **JavaScript** for responsiveness.
  


### Back end


- [Python](https://www.python.org/)
    - The project uses **Python** to write the sites logic.
  
- [Flask](http://flask.pocoo.org/)
    - The project uses the **Flask** micro web framework for the apps backend functionality.
    - 
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
    - The project uses the **Flask-PyMongo** as per instructions.
    - 
- [MongoDB](https://www.mongodb.com/)
    - The project uses the **MongoDB** for the apps database.



### Version Control



- The project uses [Git](https://git-scm.com) as it's version control system.
  
- The project uses  a  [Github](https://github.com/markwilde33) repository.




## Database Schema


##### The main MongoDB collection `recipes` has the following schema.

```json

{
    "_id": {
        "$oid": "5bb367d579c4182d22c1e738"
    },
    "country_name": "Vietnam",
    "course_type": "Dessert",
    "user_name": "Teresa May",
    "recipe_name": "Banana, Tapioca and Coconut Pudding",
    "recipe_description": "Great combination of sweet banana and chewy tapioca pearl in a rich coconut sauce.",
    "preparation_time": "5 minutes",
    "cooking_time": "30 minutes",
    "total_time": "35 Minutes",
    "servings": "8",
    "ingredients": "\r\n\r\n 1kg of very ripe asian bananas.\r\n1/2 cup sugar.\r\n1 tsp kosher salt.\r\n5 cup water.\r\n1 package 3.5 OZ dried shredded Tapioca - Soaked.\r\n1/3 cup Tapioca pearls.\r\n1-1/2 can coconut milk (13.5 OZ can).\r\n1/4 to 1/3 cup white sugar.\r\n1/4 tsp kosher salt.\r\nVanilla sugar or 3 Pandan leaves washed and tied into a knot.",
    "instructions": "Bring water and coconut milk to boil in a medium saucepan.\r\nAdd sugar, salt, tapioca.\r\nReduce heat to medium low, let it cook for about 30 minutes, stir frequently.\r\nStir in bananas, remove from heat and let stand for 15 minutes.\r\nNote: after you add the bananas, don\u2019t stir too much, it\u2019ll break up the fruit.\r\nServe hot, or chill for 3-4 hours.",
    "tags": "banana tapioca coconut",
    "allergens": "none",
    "recipe_creator": "Teresa May",
    "img_url": "https://img.taste.com.au/HAHYDv8F/w720-h480-cfill-q80/taste/2016/11/banana-coconut-tapioca-puddings-che-chuoi-33083-1.jpeg"
}
```


## Testing



<details>
      <summary><strong><em>User Story Tests</em></strong></summary>

## User Tests:

1. Verify that all recipes are vegan.
2. Verify that there are several health conscious recipes.
3. Verify that are several recipes which are simple to prepare.
4. Verify that users can store their favorite recipes on the website.
5. Verify that users would be happy to recommend the website to others interested in a plant-based diet.
6. Verify that users can edit and delete recipes.
</details> 


<details>
      <summary><strong><em>Manual Tests</em></strong></summary>

## Manual Tests:
  

#### Index Page:
   
1. Open the app.
2. Try to submit the empty register form and verify that an error message about the required fields appears.
3. Try to submit the empty login form and verify that an error message about the required fields appears.
4. Try to submit the login form  without first registering and verify that an error message appears.
5. For the registration form, verify a user receives a warning message if they enter a user name that has already been chosen by another user.
6. For the login form, verify a user receives a warning message if they enter an incorrect user name and/or password.
7. When a user successfully registers verify they are taken directly to the courses page and receive a welcome message.
8. When a user successfully logs in verify they are taken directly to the courses page and receive a welcome message.
9. Verify the link in the footer is functioning correctly. 

#### Navbar:

1. Click on the "Asian Cuisine" link, verify the Asian Cuisine page is loaded.
2. Click on the "About" link, verify the about page is loaded.
3. Click on the "My Recipes" link, verify the My Recipes page is loaded.
4. Click on the "All Recipes" link, verify the All Recipes page is loaded.
5. Click on the "By Country" link, verify the By Country page is loaded.
6. Click on the "Logout" link, verify the user is logged out and taken to the index page.

#### Add Recipe Button:
1. Verify the floating action button is displaying in the bottom left corner of all pages except the index page.
2. Verify users are taken to the add recipe page when they click on the button.
   
#### Recipe Cards:
1. Verify cards display all recipe information stored in the database.
2. Verify the view button is functioning correctly, when clicked users are taken to a full page view of the recipe.
3. Verify the edit button is functioning correctly, when clicked users are taken to the edit recipe page.
4. Verify the delete button is functioning correctly, when clicked the recipe is deleted.

#### Courses Page:

1. Verify the three course cards are displaying.
2. Click on each card and verify a user is taken to that course type, for example, if a user clicks on the starters card a separate page will load and display all starter recipe cards in the collection.

#### About Page:
   
1. Verify all information is displaying as intended with no grammatical errors.

#### My Recipes Page:
   
1. Verify any recipe a user adds or edits is displayed here.
2. Verify users are shown a picture of the recipe with the recipe name below.
3. Verify users can view, edit or delete a recipe by clicking the buttons labeled same. 

#### All Recipes Page:

1. Verify the full collection of recipe cards are displayed here.

#### By Country Page:

1. Verify the five country cards are displaying.
2. Click on each card and verify a user is taken to the chosen country, for example, if a user clicks on the Thai card a separate page will load and display all Thai recipe cards in the collection.

#### Add/Edit/My Recipe input forms:

1. Verify that all intended fields are displaying and that each field should be filled by the user with none left blank.
2. Verify a user will receive an error for any field that has not been filled.
3. Verify the add recipe and edit recipe buttons are functioning correctly, and that the database has been updated when the forms are submitted. 
   
</details> 


<details>
      <summary><strong><em>Other</em></strong></summary>


### Further Testing

- Google chrome developer tools where used at every stage of production to
isolate issues and improve mobile responsiveness.
- The app has been tested on various browsers, including Chrome, Firefox, Opera, and Safari.
- The app was tested across many screen sizes, from very small to very large.
- Some family members tested the app on their own devices and their recommendations, such as to include individual recipe images, were taken on board.
- It is displaying as intended across various devices and in different browsers.


### Issues

- The author is not yet proficient in automated testing, and as such, was unable to adhere to a test driven development approach.
- There was an issue with the full screen background image on the landing page not taking up the full viewport on some smaller mobile screens. As a result,  a media query was used to remove the background image on some smaller mobile screens.
- There was an issue hiding the app.configs for the mongo database. This issue remained unresolved and the app.configs are displayed in the app.py page.
- There were issues using pagination on the All Recipes page. As the page wasn't displaying correctly, the pagination functionality was removed.
</details> 




## Deployment



The website has been deployed to [Heroku](https://www.heroku.com) and can be accessed [here](https://flask-cookbook.herokuapp.com/)


**Heroku Deployment**


1. Create an [Heroku](https://www.heroku.com) account.

2. Create a new app 'flask-riddle' on heroku.com

3. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli):
    ``` 
    $ brew install heroku/brew/heroku
    ``` 
4. Login to heroku:
    ``` 
    $ heroku login
    ``` 
5. Check app has been created by heroku:
    ``` 
    $ heroku apps
    ``` 
6. Add heroku remote:
    ``` 
    $ heroku git:remote -a flask-riddle
    ``` 
7. Add requirements.txt file:
    ``` 
    $ sudo pip3 freeze --local > requirements.txt
    $ git add requirements.txt
    $ git commit -m " Added a requirements.txt"
    $ git push heroku master
    ``` 
8.  Add Procfile (instructs heroku how start running the project):
    ``` 
    $ echo web: python app.py > Procfile
    $ git add Procfile
    $ git commit -m 'Added Procfile'
    $ git push heroku master
    ``` 
9.  Set up dynos:
    ``` 
    $ heroku ps:scale web=1
    ``` 
10. Setup config variables on heroku dashboard:
    - Go to settings and click on reveal config vars
    - Set IP to 0.0.0.0
    - Set PORT to 5000

11. Restart dynos:
    - Navigate into the 'More' menu and select 'Restart all dynos' to update the apps settings.

12. Open app:
    - Click on the 'Open app' button to view your heroku deployed app in the browser.
  



## Installation



``` 
from the console type:

$ git clone https://github.com/markwilde33/CI-project-four
$ cd CI-project-four
$ pip3 install -r requirements.txt 
$ python3 app.py

```
App available at http://127.0.0.1:5000/




## Credits



[Code Institute](https://codeinstitute.net/)

The Html Fundamentals module, CSS Fundamentals module, Python Fundamentals module,Practical Python module and the Data Centric Development module were used for guidance.



### Content



- [VeganHeaven](https://veganheaven.org/all-recipes/50-amazing-vegan-asian-recipes/) was used for recipe information.
- [VeganRicha](https://www.veganricha.com/category/asian) was used for recipe information.



### Media

- [Google Images](https://www.google.ie/search?hl=en&authuser=0&biw=1019&bih=978&tbm=isch&sa=1&ei=phhbXO_CDeeT1fAPsMKL0AU&q=vegan+food&oq=vegan+food&gs_l=img.3..35i39l2j0l8.53715.56501..56775...0.0..0.97.929.11......1....1..gws-wiz-img.......0i67j0i5i30.n3wDW5B8r6k) was used for the cuisine pictures.



### Acknowledgements



- I received inspiration for this project from [Code Institute](https://codeinstitute.net/), [The Net Ninja](https://www.thenetninja.co.uk), [Brad Traversy](https://www.traversymedia.com/) and [Corey Schafer](https://www.youtube.com/user/schafer5/featured).
