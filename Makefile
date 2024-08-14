up:
	docker-compose.yml up -d

down:
	docker-compose.yml down && docker network prune --force

run:
	python manage.py runserver

tests:
	python manage.py test

upgrade:
	python -m pip install --upgrade pip

install:
	poetry install --no-interaction --no-ansi --no-root --with dev
