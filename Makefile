install:
	@poetry install
build:
	@poetry build
shell:
	@poetry shell
run:
	@poetry run gunicorn -w 4 task_manager.wsgi
lint:
	@poetry run flake8 task_manager/
requirements:
	@poetry export -f requirements.txt --output requirements.txt
translation:
	django-admin makemessages -l en
