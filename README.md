# Fish-Market-Detection 

### Description
Fish-Market-Detection is a web app to predict the fish species
with the help of a logistical regression model.

### Project Structure
''' bash
    │   requirments.txt
    │
    ├───FishMarketProject
    │   │   db.sqlite3
    │   │   finalFishModel.sav
    │   │   manage.py
    │   │
    │   ├───fish
    │   │   │   admin.py
    │   │   │   apps.py
    │   │   │   models.py
    │   │   │   tests.py
    │   │   │   urls.py
    │   │   │   views.py
    │   │   │   __init__.py
    │   │   │
    │   │   ├───migrations
    │   │   │   │   __init__.py
    │   │   │   │
    │   │   │   └───__pycache__
    │   │   │           __init__.cpython-38.pyc
    │   │   │
    │   │   ├───templates
    │   │   │       histo.html
    │   │   │       home.html
    │   │   │       info.html
    │   │   │       plots.html
    │   │   │       result.html
    │   │   │       test.html
    │   │   │
    │   │   └───__pycache__
    │   │           admin.cpython-38.pyc
    │   │           models.cpython-38.pyc
    │   │           urls.cpython-38.pyc
    │   │           views.cpython-38.pyc
    │   │           __init__.cpython-38.pyc
    │   │
    │   └───FishMarketProject
    │       │   asgi.py
    │       │   settings.py
    │       │   urls.py
    │       │   wsgi.py
    │       │   __init__.py
    │       │
    │       └───__pycache__
    │               settings.cpython-38.pyc
    │               urls.cpython-38.pyc
    │               wsgi.cpython-38.pyc
    │               __init__.cpython-38.pyc
    │
    └───model
        │   finalFishModel.py
        │   finalFishModel.sav
        │   Fish.csv
        │
        └───__pycache__
                fishmodel.cpython-38.pyc
 
 '''           
  

    
This structure has two root folders & requirments file :
* The *FishMarketProject* which contains all django files
* The *model* folder contains the dataset and the trained model(Logistic Regression)

## Getting Started
### Pre-requisites and Local Development
* run pip install -r requirements.txt to install all packages and libraries needed for the project 
* navigate to model the run python finalFishModel.py 
* navigate to FishMarketProject 
  ** run python manage.py makemigrations 
  ** run python manage.py migrate 
  ** run python manage.py runserver 
  
  ## The application is run at http://127.0.0.1:8000/
  

.
