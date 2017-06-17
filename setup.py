import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.org')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-gpg',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'Django==1.11.2',
        'gnupg==2.3.0',
    ],
    include_package_data=True,
    license='GPLv3',
    description='GPG Support for Django',
    long_description=README,
    url='https://github.com/arecker/django-gpg',
    author='Alex Recker',
    author_email='alex@reckerfamily.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
