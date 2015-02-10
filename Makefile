.PHONY: test clean

help:
	@echo "Run make test|clean"

test: pytest clean

pytest:
	py.test

clean:
	find . -type f -name '*.pyc' -print0 | xargs -0 rm -f
	find . -type d -name '*__pycache__*' -print0 | xargs -0 rmdir --ignore-fail-on-non-empty
