PROJECT_NAME = {{ project_name }}
TEST_APPS = core

test:
	python manage.py test $(TEST_APPS)

run:
	python manage.py runserver 0.0.0.0:8000

migrate:
	python manage.py migrate

shell:
	python manage.py shell

syncdb:
	python manage.py syncdb

mailserver:
	python -m smtpd -n -c DebuggingServer 0.0.0.0:1025

collectstatic:
	python manage.py collectstatic

manage:
	python manage.py $(CMD)
