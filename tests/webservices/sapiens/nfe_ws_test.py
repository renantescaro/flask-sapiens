import unittest
import sys
sys.path.append('C:/Users/renan.tescaro/Desktop/flask/flask-sapiens/')

from flaskr.webservices.sapiens.nfe_ws import NfeSapiensWs
from flaskr.entities.sapiens.nfe import NfeSapiens
from flaskr.dao.faturamento_dao import FaturamentoDao

class NfeSapiensWsTest:
    def __init__(self):

        dados = FaturamentoDao().pedido_com_produtos_faturar_nfe(
            id_ped_sapiens='3628' )

        requisicao = NfeSapiens.parametros_requisicao(dados)
        retorno    = NfeSapiensWs().gravar_notas_fiscais_saida(requisicao)

        # print(requisicao)
        print(retorno)
        if retorno['erroExecucao'] == None:
            print('ok!')
        else:
            print('erro!')

        print(retorno['mensagemRetorno'])

NfeSapiensWsTest()