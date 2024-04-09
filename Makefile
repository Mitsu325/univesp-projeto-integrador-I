all:
	/usr/bin/python3 manage.py runserver

mg:
	/usr/bin/python3 manage.py migrate

load:
	/usr/bin/python3 manage.py loaddata genders_fixture.json
	/usr/bin/python3 manage.py loaddata education_level_fixture.json
