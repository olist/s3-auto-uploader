import codecs
import os
import re

from setuptools import setup, find_packages, Command

here = os.path.abspath(os.path.dirname(__file__))

package = 's3_auto_uploader'
install_requires = [
    'boto3==1.4.0',
    'botocore==1.4.51',
    'watchdog==0.8.3',
]
tests_require = [
    'pytest',
    'pytest-cov',
    'vcrpy',
]

version = "0.0.0"
changes = os.path.join(here, "CHANGES.rst")
match = r'^#*\s*(?P<version>[0-9]+\.[0-9]+(\.[0-9]+)?)$'
with codecs.open(changes, encoding='utf-8') as changes:
    for line in changes:
        res = re.match(match, line)
        if res:
            version = res.group("version")
            break

# Get the long description
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get version
with codecs.open(os.path.join(here, 'CHANGES.rst'), encoding='utf-8') as f:
    changelog = f.read()


class VersionCommand(Command):
    description = "print library version"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(version)


setup(
    name='olist-fixtures',
    version=version,
    description='Generate fixtures for Olist V2 API',
    long_description=long_description,
    url='https://github.com/solidarium/olist-fixtures',
    author='Olist Developers',
    author_email='developers@olist.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='amazon s3 monitoring watcher filesystem',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=install_requires,
    setup_requires=['pytest-runner', 'pytest'],
    test_suite='tests',
    tests_require=tests_require,
    cmdclass={
        "version": VersionCommand,
    },
)
