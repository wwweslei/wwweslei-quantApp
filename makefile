clean:
	pip install -e .[dev] --upgrade --no-cache

install:
	pip install -e .['dev']

tests:
	pytest tests/ -v  