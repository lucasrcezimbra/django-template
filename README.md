# Django Template
[![Updates](https://pyup.io/repos/github/Lrcezimbra/django-template/shield.svg)](https://pyup.io/repos/github/Lrcezimbra/django-template/)

An opinionated Django start project template that uses:
- [python-decouple](https://github.com/henriquebastos/python-decouple) to organize settings and decouple from code
- [dj-database-url](https://github.com/kennethreitz/dj-database-url) to cast database URL to Django setting
- [django-extensions](https://github.com/django-extensions/django-extensions) for custom extensions for Django
- [pytest-django](https://github.com/pytest-dev/pytest-django) and [pytest-mock](https://github.com/pytest-dev/pytest-mock) for tests


## How to Use
```
PROJECT=myproject \
        && django-admin startproject --template=https://github.com/Lrcezimbra/django-template/archive/master.zip --extension=env,txt $PROJECT \
        && cd $PROJECT \
        && python -m venv .venv \
        && source .venv/bin/activate \
        && pip install -r requirements.txt \
        && python manage.py runserver
```

## Contribute

Contributions are welcome, feel free to suggest improvements.


##

[ ~ Dependencies scanned by PyUp.io ~ ]
