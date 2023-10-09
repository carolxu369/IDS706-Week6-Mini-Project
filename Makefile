# Makefile

setup:
	pip install -r requirements.txt

test:
	python -m unittest discover -s tests -p "*_test.py"

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

run:
	python main.py