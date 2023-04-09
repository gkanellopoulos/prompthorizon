import os
from setuptools import setup, find_packages

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        return f.read()


setup(
    name='prompt-horizon',
    version='0.1.4',
    description='Library to anonymize JSON objects by creating placeholders for keys and values, while generating a reversible mapping to restore afterwards',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
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