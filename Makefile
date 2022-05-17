create_db:
	flask create-db

run:
	flask run

run_process:
	flask update-posts-process

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements_dev.txt
	pip install -r requirements_test.txt
	flask create-db

lint:
	black .
	flake8 --max-line-length=120 .
	isort .

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build