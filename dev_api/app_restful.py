from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

devs= [
    {'id':0,'nome':'Keven','habilidades': ['Python', 'Flask']},
    {'id':1,'nome':'Salino','habilidades': ['Java', 'Go']}
]

#Não utiliza rotas no modelo convencional
class Dev(Resource):
    def get(self,id):
        try:
            response = devs[id]
            print(response)
        except IndexError:
            response = {'status': 'erro','mensagem': 'Desenvolvedor de ID {} nao existe'.format(id) }
        except Exception:
            response = {'status': 'erro','mensagem': 'Erro desconhecido'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        devs[id] = dados
        return dados

    def delete(self, id):
        devs.pop(id)
        return {'status': 'sucesso', 'mensagem':'Registro excluido!'}



class List_Dev(Resource):
    def get(self):
        return devs

    def post(self):
        dados = json.loads(request.data)
        position = len(devs)
        dados['id'] = position
        devs.append(dados)
        return devs[position]

#Rota RESTful
api.add_resource(Dev, '/dev/<int:id>/')
api.add_resource(List_Dev, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)