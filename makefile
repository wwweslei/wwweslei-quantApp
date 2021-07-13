install:
	pip install -e .['dev']

tests:
	pytest tests/ -v
db:
	flask db init
	flask db migrate
	flask db upgrade