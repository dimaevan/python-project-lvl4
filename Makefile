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
	@poetry run flake8 task_manager/
requirements:
	@poetry export -f requirements.txt --output requirements.txt
translation:
	django-admin makemessages -l en
compile:
	django-admin compilemessages
test:
	@poetry run pytest tests/ -svv