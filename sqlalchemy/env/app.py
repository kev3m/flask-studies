from urllib import response
from flask import Flask 
from flask_restful import Resource, Api, request
from models import Pessoas
import json

app = Flask(__name__)
api =  Api(app)

class Pessoa(Resource):
    def get(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status':'error',
                'mensage':'Pessoa não encontrada'
            }
        return response

    def put(self,nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

    def delete(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        response = 'Pessoa {} excluida com sucesso'.format(pessoa.nome)
        return {'status': 'success', 'mensagem':response}

class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response

    def post(self):
        data = request.json
        pessoa = Pessoas(nome=data['nome'], idade=data['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')

if __name__ == '__main__':
    app.run(debug=True)



