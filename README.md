
# PurBeurre

PurBeurre is a web-app that helps you improve your diet. It's based on DB Openfoodfacts, so you can choose a food from your diet and replace it with another that has a better nutriscore.

## Prerequisites

-   Python 3.7
-   Django 2.1+ (2.1.7 used for developpement)
-   PostGreSQL
-   All the other required modules are in the requirements.txt file to install before launching the app.

## How to install

After download the project put the following commands to run on localhost:

    pip install -r requirements.txt
    cd ./pur_beurre
    ./manage.py init_db
    ./manage.py runserver

You can check pur_beurre at http://127.0.0.1:8000/
    
 ## Deployment

To deploy this project on heroku uncomment line 14, 31 and 138 of settings.py and run the following command

    git commit -am 'your commit message'
    git push heroku master

## Availability

[Here](https://mysterious-island-48225.herokuapp.com/)