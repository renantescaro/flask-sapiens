from flaskr.entities.sapiens.nfe import NfeSapiens
from zeep import Client
from flaskr.webservices.sapiens.config import ConfigSapiensWs

class NfeSapiensWs:
    def __init__(self):
        self._config = ConfigSapiensWs()
        self._client = Client( self._config.url+str('sapiens_Synccom_senior_g5_co_mcm_ven_notafiscal?wsdl') )

    def obter_faturamento(self, data_inicio:str, data_final:str):
        return self._client.service.obterFaturamento(
            user       = 'sidecomm',
            password   = 'sidecomm',
            encryption = '',
            parameters = {
                'dataInicio' : data_inicio,
                'dataFim'    : data_final } )

    
    def gravar_notas_fiscais_saida(self, nfe_sapiens: NfeSapiens):
        return self._client.service.GravarNotasFiscaisSaida_12(
            user       = 'sidecomm',
            password   = 'sidecomm',
            encryption = '',
            parameters = nfe_sapiens.parametros_requisicao() )