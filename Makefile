clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

delete-cassettes:
	@rm -rf resources/cassettes/*

enable-dev: delete-cassettes
	@cp dev.env .env

enable-local: delete-cassettes
	@cp local.env .env

test:
	python setup.py test

build: test
	pip install -U wheel
	python setup.py sdist
	python setup.py bdist_wheel

/usr/local/bin/package_cloud:
	sudo gem install package_cloud

package_cloud: /usr/local/bin/package_cloud

release: package_cloud clean build
	git rev-parse --abbrev-ref HEAD | grep '^master$$'
	git tag `python setup.py -q version`
	git push origin `python setup.py -q version`
	package_cloud push olist/v2/python dist/*.whl
	package_cloud push olist/v2/python dist/*.tar.gz
