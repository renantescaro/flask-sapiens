from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='flaskr',
    version='1.1',
    author='Renan Tescaro',
    author_email='renantescaro@hotmail.com',
    description='Aplicação para testar Ambiente com ERP Sapiens',
    packages=['flaskr'],
    install_requires=required
)