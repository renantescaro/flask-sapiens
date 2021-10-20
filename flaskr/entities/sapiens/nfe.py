import json

class NfeSapiens:
    def parametros_requisicao(dados):
        parametros = {
            'tipoProcessamento'    : 4,
            'identificacaoSistema' : 'EC',
            'dadosGerais'  : {
                'codEmp'   : 1,
                'codFil'   : 1,
                'codSnf'   : 'ECO',
                'numNfv'   : '',
                'codRep'   : 999,
                'codCli'   : dados[0]['CODCLI'],
                'codEdc'   : '55',
                'produtos' : [] } }

        produto = []
        for p in dados:
            produto.append( {
                'filPed' : 2,
                'numPed' : p['NUMPED'],
                'codPro' : p['CODPRO'],
                'codDer' : p['CODDER'],
                'seqIpd' : p['SEQIPD'],
                'qtdFat' : p['QTDVEN'] } )
        parametros['dadosGerais']['produtos'] = produto
        return parametros