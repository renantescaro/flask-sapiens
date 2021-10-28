import cx_Oracle
from flaskr.utils.config import Config


class Banco:
    def __init__(self):
        self._ip       = str(Config.get('BANCO_IP'))
        self._port     = str(Config.get('BANCO_PORTA'))
        self._username = str(Config.get('BANCO_USUARIO'))
        self._password = str(Config.get('BANCO_SENHA'))
        self._bd       = str(Config.get('BANCO_BANCO'))
        self._conn     = self._criar_conexao()
        self._cursor   = self._conn.cursor()


    def _criar_conexao(self):
        try:
            dsn = cx_Oracle.makedsn(self._ip, self._port, self._bd)
            return cx_Oracle.connect(
                user     = self._username,
                password = self._password,
                dsn      = dsn )

        except cx_Oracle.Error as err:
            print(err)
            return None


    def executar(self, query):
        if self._cursor is not None:
            self._cursor.execute(query)
            dados = self._cursor.fetchall()
            self._conn.close()
            return dados
        return None