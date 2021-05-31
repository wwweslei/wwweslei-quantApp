install:
	pip install -e .['dev']

tests:
	pytest tests/ -v  