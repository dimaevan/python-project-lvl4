install:
	@poetry install
build:
	@poetry build
shell:
	@python manage.py shell_plus --plain
run:
	@poetry run gunicorn -w 4 task_manager.wsgi :8080
lint:
	@poetry run flake8 task_manager/
requirements:
	@poetry export -f requirements.txt --output requirements.txt
translation:
	django-admin makemessages -l en
