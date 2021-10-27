from flask import Blueprint, json

from flaskr.dao.faturamento_dao import FaturamentoDao

bp = Blueprint(
    'faturamento',
    __name__,
    template_folder='templates')


class FaturamentoCtrl:
    @bp.route('/', methods=['GET'])
    def json():
        dados = FaturamentoDao().pedido_com_produtos_faturar_nfe(9924)
        return json.dumps(dados)


    @bp.route('/html', methods=['GET'])
    def html():
        return '<h1>Página html</h1>'