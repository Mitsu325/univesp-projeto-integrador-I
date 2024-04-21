all:
	/usr/bin/python3 manage.py runserver

install:
	pip install -r requirements.txt

mg:
	/usr/bin/python3 manage.py migrate

load:
	/usr/bin/python3 manage.py loaddata genders_fixture.json
	/usr/bin/python3 manage.py loaddata education_level_fixture.json
	/usr/bin/python3 manage.py loaddata state_fixture.json
	/usr/bin/python3 manage.py loaddata city_fixture.json
	/usr/bin/python3 manage.py loaddata languages_fixture.json
	/usr/bin/python3 manage.py loaddata tech_skill_fixture.json
	/usr/bin/python3 manage.py loaddata course_fixture.json
	/usr/bin/python3 manage.py loaddata job_title_fixture.json
	/usr/bin/python3 manage.py loaddata area_of_interest_fixture.json
	/usr/bin/python3 manage.py loaddata manager_fixture.json
