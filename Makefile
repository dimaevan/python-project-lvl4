install:
	@poetry install
build:
	@poetry build
shell:
	@poetry shell
run:
	python manage.py runserver
lint:
	@poetry run flake8 task_manager/
requirements:
	@poetry export -f requirements.txt --output requirements.txt