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