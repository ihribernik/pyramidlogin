.PHONY: clean virtual-env system-packages python-packages install tests run generate-db generate-data all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
	find . -name '__pycache__' -delete
	rm -rf *.egg-info dist build

system-packages:
	sudo apt install python-pip -y

virtual-env:
	virtualenv env
	. env/bin/activate

python-packages:
	pip install --upgrade pip setuptools
	pip install -e ".[testing]"

install: system-packages virtual-env python-packages

generate-db:
	alembic -c development.ini revision --autogenerate -m "init"
	alembic -c development.ini upgrade head

generate-data:
	initialize_pyramidlogin_db development.ini

tests:
	pytest

run:
	pserve development.ini --reload

all: clean install tests run