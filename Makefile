run:
	docker-compose -f docker-compose.yml up --build

run-admin:
	docker-compose -f docker-compose.yml -f docker-compose.admin.yml up --build

migrate-create:
	docker-compose exec server python manage.py makemigrations catalog

migrate-apply:
	docker-compose exec server python manage.py migrate

shell:
	docker-compose exec server python manage.py shell

test:
	docker-compose exec server python manage.py test

load-data:
	docker-compose exec server \                                                                                                                                                 <aws:of-prod>
		python manage.py loaddata \
			catalog/fixtures/wines.json \
			--app catalog \
			--format json

pgcli:
	pgcli postgres://perusable:perusable@localhost:5433/perusable
