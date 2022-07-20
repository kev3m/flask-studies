from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tasks = [
    {
    'id': 0,
    'responsavel': 'Dev',
    'tarefa': 'Do something',
    'status': 'pendente'
    },
    {
    'id': 1,
    'responsavel': 'Office-boy',
    'tarefa': 'warm coffee time',
    'status': 'pendente'
    }
]

@app.route('/tasks/', methods=['GET', 'POST'])
def built_tasks():
    if request.method == 'GET':
        return jsonify(tasks)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        position = len(tasks)
        dados['id'] = position
        tasks.append(dados)
        return('Task adicionada com sucesso!')

@app.route('/tasks/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def modifyTasks(id):
    if request.method == 'GET':
        try:
            return tasks[id]
        except Exception:
            return ('Não foi possivel localizar a tarefa!')
    elif request.method == 'PUT':
        if tasks[id]['status'] == 'concluido':
            tasks[id]['status'] == 'pendente'
        elif tasks['status'][id] == 'pendente':
            tasks[id]['status'] == 'concluido'
        return ('O status da tarefa {} teve seu status alterado'.format(id))
        

#json.loads - transforma uma string válida json em um objeto dicionário

if __name__ == '__main__':
    app.run(debug=True)