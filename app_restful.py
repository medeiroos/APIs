from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':'0',
        'nome': 'Gabriel',
        'habilidaddes': ['Python', 'Flask']
     },
    {
        'id':'1',
        'nome': 'Rafael',
        'habilidades': ['Python', 'Django']
     }
]

# DEVOLVE UM DESENVOLVEDOR PELO ID, TAMBEM ALTERA E DELETA UM DESENVOLVEDOR
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'ERRO', 'mensagem':'Desenvolvedor de ID {} não existe'.format(id)}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'ERRO', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído!'}


# LISTA TODOS OS DESENVOLVEDORES E TAMBEM CRIA UM NOVO DESENVOLVEDOR
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/lista/')
if __name__ == '__main__':
    app.run(debug=True)
