import unittest
import sys
sys.path.append('C:/Users/renan.tescaro/Desktop/flask/flask-sapiens')

from flaskr.webservices.sapiens.nfe_ws import NfeSapiensWs
from flaskr.entities.sapiens.nfe import NfeSapiens

class NfeSapiensWsTest:
    def __init__(self):
        nfe_sapiens = NfeSapiens()
        nfe_sapiens
        nfe_sapiens
        nfe_sapiens
        nfe_sapiens
        nfe_sapiens
        nfe_sapiens
        nfe_sapiens
        retorno = NfeSapiensWs().gravar_notas_fiscais_saida(nfe_sapiens)
        print(retorno)

NfeSapiensWsTest()