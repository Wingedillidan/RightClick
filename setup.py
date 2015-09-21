try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My first steps into Pygame',
    'author': 'Collin McLean',
    'url': 'http://github.com/wingedillidan/PROJECT',
    'author_email': 'wingedillidan@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Project: Right Click'
}

setup(**config)
