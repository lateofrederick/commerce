# Commerce
A django web app

## Introduction
This document describes the steps involved in setting up a local development environment for commerce.

### 1) Create Virtualenv and Install python requirements
```
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip3 install wheel
(.venv) $ pip3 install -r requirement.txt
```

### 3) Create a local_config python file with the following configurations
```
ALLOWED_HOST = []

SECRET_KEY = 'django-insecure-dfyqbmfsjm#pnc#bmie#tce58bdlw1n%7jr!c!dgrbwhl6gqf('

DEBUG = TRUE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'store',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

### 3) Run migrations
$ python manage.py migrate

### 3) Load fixtures in this order
$ python manage.py loaddata commerce/fixtures/group.json


### 3) Run development server
```
$ python3 manage.py runserver
```

### Assumptions and tradeoffs made
```
- We have one seller on the platform but multiple buyers
- Use mysql instead of postgres due to deployment issues
- cannot perform full text search on mysql in django, so text search
  only works locally
- have api keys and other keys in plain text to avoid a lot of setup in
    production environment due to time limit
- email notification will through error if email is not known
- aggregation of books sums and counts is mildly done, leading to a lot of
    similar books in data rendering
- log out system not added
```





