lint:
	black modelkit_imdb tests
	isort --profile black modelkit_imdb tests
	flake8 modelkit_imdb tests
	mypy modelkit_imdb

test:
	pytest

coverage:
	coverage run -m pytest
	coverage report -m
