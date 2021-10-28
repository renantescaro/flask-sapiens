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


### Configurações
* arquivo .env

<br>

### Executar aplicação
* > python3.7 run.py

<br>
<br>

## Publicar aplicação
* > python setup.py bdist_wheel
#### Arquivo gerado
* > dist/flaskr-1.0-py3-none-any.whl


#### Copiar projeto inteiro via SSH
* > scp -r seu_diretorio_local usuario_servidor@ip_servidor:caminho_servidor
#### Copiar arquivo via SSH
* > scp -r seu_diretorio_local/flask-sapiens/dist/flaskr-1.0-py3-none-any.whl usuario_servidor@ip_servidor:caminho_servidor
* Exemplo: scp -r C:/Users/renan.tescaro/Desktop/flask/flask-sapiens/ root@192.168.1.212:/home/apps/

<br>

#### No servidor em produção
* > pip install flaskr-1.0-py3-none-any.whl
* > waitress-serve --call 'flaskr:create_app'