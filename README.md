### Estrutura simples para teste com Webservice do Sapiens
* Python 3.7.3
* Flask 1.1.2

<br>

### Instalar todas as dependências
* pip install -r requirements.txt

<br>

### Instalar dependências manualmente
* > pip install zeep
* > pip install cx-Oracle
* > pip install wheel
* > pip install waitress

<br>

### Executar aplicação em desenvolvimento
* Windows
* > set FLASK_APP=flaskr
* > set FLASK_ENV=development
* > set FLASK_RUN_HOST=192.168.1.182
* > set FLASK_RUN_PORT=80
* > flask run

<br>

* Linux
* > export FLASK_APP=flaskr
* > export FLASK_RUN_HOST=192.168.1.212
* > export FLASK_RUN_PORT=5000
* > flask run

<br>

#### Publicar aplicação
* > python setup.py bdist_wheel
#### Arquivo gerado
* > dist/flaskr-1.0-py3-none-any.whl

<br>

#### Copiar projeto inteiro via SSH
* > scp -r C:/Users/renan.tescaro/Desktop/flask/flask-sapiens/dist/ root@192.168.1.212:/home/apps/
#### Copiar arquivo via SSH
* > scp -r C:/Users/renan.tescaro/Desktop/flask/flask-sapiens/dist/flaskr-1.0-py3-none-any.whl root@192.168.1.212:/home/apps/

<br>

#### No servidor em produção
* > pip install flaskr-1.0-py3-none-any.whl
* > waitress-serve --call 'flaskr:create_app'