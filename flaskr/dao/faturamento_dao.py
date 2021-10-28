import collections
from flaskr.dao.banco import Banco


class FaturamentoDao(Banco):
    def pedido_com_produtos_faturar_nfe(self, id_ped_sapiens:int):
        query = """ 
            SELECT 
                ped.CODCLI, ped.NUMPED,
                item.CODPRO, item.CODDER,
                ped.CODFIL, item.SEQIPD,
                item.QTDVEN 
            FROM SAPIENS.E120IPD item
            INNER JOIN SAPIENS.E120PED ped
            ON ped.NUMPED = item.NUMPED 
            WHERE item.NUMPED = '"""+str(id_ped_sapiens)+"""'
            AND item.CODREP = 999
            AND item.CODEMP = 1
            """

        objects_list = []
        for row in self.executar(str(query)):
            d = collections.OrderedDict()
            d['CODCLI'] = row[0]
            d['NUMPED'] = row[1]
            d['CODPRO'] = row[2]
            d['CODDER'] = row[3]
            d['CODFIL'] = row[4]
            d['SEQIPD'] = row[5]
            d['QTDVEN'] = row[6]
            objects_list.append(d)
        return objects_list