install:
	@poetry install
build:
	@poetry build
shell:
	@python manage.py shell_plus --plain
run:
	@python ./manage.py runserver
rung:
	@poetry run gunicorn -w 4 task_manager.wsgi
lint:
	@poetry run flake8 task_manager/ labels/ statuses/ tasks/ templates/ tests/
requirements:
	@poetry export -f requirements.txt --output requirements.txt
translation:
	django-admin makemessages -l en
compile:
	django-admin compilemessages

test:
	@poetry run pytest tests/ -svv
testt:
	@poetry run pytest tests/test_users.py -svv
test-cov:
	@poetry run pytest --cov=. --cov-report xml

m:
	@python manage.py migrate
mm:
	@python manage.py makemigrations
su:
	@python manage.py createsuperuser

gt:
	@python manage.py makemessages -a
tr:
	@python manage.py compilemessages
