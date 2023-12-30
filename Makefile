MANAGE := poetry run python manage.py


.PHONY: install
install:
	poetry install

.PHONY: setup
setup:	
	install migrate

.PHONY: migrate
migrate:
	$(MANAGE) migrate

.PHONY: makemigrations
makemigrations:
	$(MANAGE) makemigrations

.PHONY: serv
serv:
	poetry run gunicorn -w 5 -b 0.0.0.0:10000 task_manager.wsgi:application

.PHONY: dev
dev:
	$(MANAGE) runserver

build:
	./build.sh

.PHONY: coverage
coverage:
	poetry run coverage run manage.py test task_manager/users -v 2

test:
	$(MANAGE) test --traceback -v 2

.PHONY: makemessages 
makemessages:
	# Use compilemessages when updated translation
	poetry run django-admin makemessages -l ru

.PHONY: compilemessages
compilemessages:
	poetry run django-admin compilemessages --ignore=.venv

.PHONY: lint
lint:
	poetry run flake8 task_manager --exclude migrations

.PHONY: test-coverage
test-coverage:
	poetry run coverage run --source='task_manager' manage.py test task_manager
	poetry run coverage xml
