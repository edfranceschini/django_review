# Django Review

Django-review is a review platform to users posts their companies reviews and rate them. 

## Getting Started

These are the steps to get started with django-reviews:

### Prerequisites
Modules to be installed in your environment:
```
djangorestframework
markdown
coreapi
coreapi-cli
pytest
pytest-django
pytest-cov
WebTest
```


### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
pip install -r requirements.txt
```

create the database:

```
python manage.py makemigrations
python manage.py migrate
```

You also need to create a superuser in order to have admin access:

```
python manage.py create super user
``` 


## Running the tests

The test system is based in pytest and covers 100% of the application

when running tests all models, views and URLS will be tested, and this is the output you should get:

```
----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                        Stmts   Miss  Cover
-----------------------------------------------
django_review/__init__.py       0      0   100%
django_review/settings.py      19      0   100%
django_review/urls.py           5      0   100%
django_review/wsgi.py           4      0   100%
-----------------------------------------------
TOTAL                          28      0   100%

```



## Deployment

To run the system you should:

```
python manage.py runserver
```

## Built With

* [Django project](https://www.djangoproject.com/) - The web framework used
* [Django REST framework ](https://www.django-rest-framework.org/) - API an RESTful 
* [Pytest](https://docs.pytest.org/en/latest/) - Used to generate automated tests

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Edson Franceschini** - *Initial work* - [My GITHUB](https://github.com/edfranceschini)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


