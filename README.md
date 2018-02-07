# Django Template
[![Updates](https://pyup.io/repos/github/Lrcezimbra/django-template/shield.svg)](https://pyup.io/repos/github/Lrcezimbra/django-template/)

An opinionated Django start project template that uses:
- [python-decouple](https://github.com/henriquebastos/python-decouple) to organize settings and decouple from code
- [dj-database-url](https://github.com/kennethreitz/dj-database-url) to cast database URL to Django setting
- [django-extensions](https://github.com/django-extensions/django-extensions) for custom extensions for Django
- [pytest-django](https://github.com/pytest-dev/pytest-django) for tests


## How to Use
### Django 2.0
Create project with Django 2.0
```
django-admin startproject --template=https://github.com/Lrcezimbra/django-template/archive/django-2.0.zip --extension=env,txt myproject
```
### Django 1.11
Create project with Django 1.11
```
django-admin startproject --template=https://github.com/Lrcezimbra/django-template/archive/django-1.11.zip --extension=env,txt myproject
```

## Contribute

Contributions are welcome, feel free to suggest improvements.
