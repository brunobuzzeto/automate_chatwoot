from setuptools import setup, find_packages

setup(
    name='automate_chatwoot',
    version='0.1.0',
    author='Bruno Buzzeto',
    author_email='brunobuzzeto.dev@gmail.com',
    description='A CLI tool for automating tasks in Chatwoot',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'automate_chatwoot=main:main',
        ],
    },
    tests_require=[
        'pytest==6.2.5',
        'psycopg2'
    ],
)
