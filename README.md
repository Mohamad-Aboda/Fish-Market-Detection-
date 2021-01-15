# Fish-Market-Detection 

### Description
    Fish-Market-Detection is a web app to predict the fish species
    with the help of a logistic regression model.

### Sample Data 
      Species  Weight  Length1  Length2  Length3   Height   Width
      Perch   135.0     20.0     22.0     23.5   5.8750  3.5250
      Perch  1000.0     39.8     43.0     45.2  11.9328  7.2772
      Smelt    10.0     11.3     11.8     13.1   2.2139  1.2838
      Bream   720.0     32.0     35.0     40.6  16.3618  6.0900
      Perch   320.0     27.8     30.0     31.6   7.6156  4.7716
      
### Species Type 
    ![Species type](https://user-images.githubusercontent.com/41721894/104699863-05075700-571c-11eb-991c-6c3a922fc194.png)


### Project Structure
```

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
```


    
This structure has two root folders & requirments file :
* The *FishMarketProject* which contains all django files
* The *model* folder contains the dataset and the trained model(Logistic Regression)

## Getting Started
### Pre-requisites and Local Development Server
* run pip install -r requirements.txt to install all packages and libraries needed for the project 
* navigate to model then run python finalFishModel.py 
* navigate to FishMarketProject 
     *run python manage.py makemigrations 
     * run python manage.py migrate 
     * run python manage.py runserver 
  
  ## The application is run at http://127.0.0.1:8000/
  
  ## Result 
  ![result](https://user-images.githubusercontent.com/41721894/104440796-766bcc00-559b-11eb-8c0c-08d5aa5acfec.gif)


.
