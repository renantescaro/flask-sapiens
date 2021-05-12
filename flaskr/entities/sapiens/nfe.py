import json

class Produto:
    def __init__(self):
        self.num_ped: int
        self.cod_pro: str
        self.cod_der: str
        self.fil_ped: int
        self.seq_ipd: int
        self.qtd_fat: int


class DadosGerais:
    def __init__(self):
        self.cod_emp: int
        self.cod_fil: int
        self.cod_rep: int
        self.cod_snf: str
        self.num_nfv: str
        self.cod_cli: str
        self.cod_edc: str
        self.produtos: list[Produto]


class NfeSapiens:
    def __init__(self):
        self.tipo_processamento: int
        self.identificacao_sistema: str
        self.dados_gerais: DadosGerais


    def parametros_requisicao(self):
        # hoje    filial 2
        # segunda filial 1
        parametros = {
            'tipoProcessamento' : self.tipo_processamento,
            'identificacaoSistema' : self.identificacao_sistema,
            'dadosGerais' : {
                'codEmp' : self.dados_gerais.cod_emp,
                'codFil' : self.dados_gerais.cod_fil,
                'codSnf' : self.dados_gerais.cod_snf,
                'numNfv' : self.dados_gerais.num_nfv,
                'codRep' : self.dados_gerais.cod_rep,
                'codCli' : self.dados_gerais.cod_cli,
                'codEdc' : self.dados_gerais.cod_edc } }

        posi = 0
        for produto in self.dados_gerais.produtos:
            parametros[posi]['produtos'] = {
                'numPed' : produto.num_ped,
                'codPro' : produto.cod_pro,
                'codDer' : produto.cod_der,
                'filPed' : produto.fil_ped,
                'seqIpd' : produto.seq_ipd,
                'qtdFat' : produto.qtd_fat,
            }
            posi = posi+1

        print(parametros)