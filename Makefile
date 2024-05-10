SHELL := /bin/bash -c



say-hello:
	@echo "Hello UD"

lint-code:
	find mlops_ud/ -name "*.py" | xargs pylint

format-code:
	black mlops_ud/

test-code:
	pytest -v mlops_ud/tests/

generate-requirements:
	poetry export -f requirements.txt --output requirements.txt

pre-commit:
	pre-commit run --all-files