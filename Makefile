# Makefile

setup:
	pip install -r requirements.txt

test:
	python -m pytest
	
lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

run:
	python main.py