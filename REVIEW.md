# Project Review

## Dependencies

Generate a requirements.txt file
to keep list of dependencies used in the project

```
pip freeze > requirements.txt
```

## Database

Explain a README file how to create a new
database for other developers in their machine
By sharing steps/commands

## Models

Likes

- LikedItem

Store

- Promotion
- Collection
- Product
- Customer
- Order
- OrderItem
- Address
- Cart
- CartItem

Playground

Tags

- Tag
- TaggedItem

## Tests

You need to add automatic tests for your models to make sure they work as expected.

## Pyproject.toml

Create a new file called pyproject.toml.

```
[tool.black]
line-length = 79
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
```

## Syntax check

I installed black to check the syntax and you can fix the followings:

```
21 files would be reformatted, 21 files would be left unchanged.
(venv) Laptop% black --check .
storeplace/likes/apps.py
storeplace/playground/urls.py
storeplace/likes/models.py
storeplace/manage.py
storeplace/store/apps.py
storeplace/playground/views.py
storeplace/asgi.py
storeplace/settings.py
storeplace/storeplace/urls.py
storeplace/playground/apps.py
storeplace/tags/apps.py
storeplace/storeplace/wsgi.py
storeplace/store/models.py
storeplace/tags/models.py

Oh no! 💥 💔 💥
```