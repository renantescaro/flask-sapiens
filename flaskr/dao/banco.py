import cx_Oracle
from flaskr.utils.config import Config


class Banco:
    def __init__(self):
        self._ip       = Config.get('banco_ip')
        self._port     = Config.get('banco_porta')
        self._bd       = Config.get('banco_nome')
        self._username = Config.get('banco_usuario')
        self._password = Config.get('banco_senha')
        self._conn     = self._criar_conexao()
        self._cursor   = self._conn.cursor()


    def _criar_conexao(self):
        dns = cx_Oracle.makedsn(self._ip, self._port, self._bd)
        self._conn = cx_Oracle.connect(self._username, self._password, dns)
        return self._conn


    def executar(self, query):
        self._cursor.execute(query)
        dados = self._cursor.fetchall()
        self._conn.close()
        return dados