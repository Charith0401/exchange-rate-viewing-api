poetry install
poetry run python manage.py loaddata postgres_dump.json
poetry run python manage.py runserver