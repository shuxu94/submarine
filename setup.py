try:
	from setuptools import setup
except ImportError:
	from distutil.core import setup

config = {
	'description': 'My Project',
	'author': 'Shu Xu',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'shu.xu94@gmail.com'
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)
