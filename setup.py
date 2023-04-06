from setuptools import setup, find_packages

setup(
    name='prompthorizon',
    version='0.1.0',
    description='A library for anonymizing and de-anonymizing JSON data',
    author='George Kanellopoulos',
    author_email='george@gkanellopoulos.com',
    url='https://github.com/gkanellopoulos/prompthorizon.git',
    packages=find_packages(),
    install_requires=[
        # List your library's dependencies here, e.g.:
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)