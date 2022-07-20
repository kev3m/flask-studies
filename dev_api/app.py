from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id':'0','nome':'Keven','habilidades': ['Python', 'Flask']},
    {'id':'1','nome':'Salino','habilidades': ['Java', 'Go']}
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
#Devolve um dev pelo ID, também altera e deleta um dev
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
            print(response)
        except IndexError:
            response = {'status': 'erro','mensagem': 'Desenvolvedor de ID {} nao existe'.format(id) }
        except Exception:
            response = {'status': 'erro','mensagem': 'Erro desconhecido'}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem':'Registro excluido!'})

#Lista os devs e registra novos devs
@app.route('/dev/', methods=['POST', 'GET'])
def lista_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        position = len(desenvolvedores)
        dados['id'] = position
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[position])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)