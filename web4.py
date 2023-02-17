from flask import Flask, request, jsonify

app = Flask(__name__)

# Dados de exemplo
alunos = [
    {
        'id': 1,
        'nome': 'João',
        'idade': 20,
        'curso': 'Engenharia'
    },
    {
        'id': 2,
        'nome': 'Maria',
        'idade': 22,
        'curso': 'Ciência da Computação'
    }
]

# Rota para listar todos os alunos
@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(alunos), 200

# Rota para obter um aluno específico
@app.route('/alunos/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    aluno = [aluno for aluno in alunos if aluno['id'] == aluno_id]
    if len(aluno) == 0:
        return jsonify({'mensagem': 'Aluno não encontrado'}), 404
    return jsonify(aluno[0]), 200

# Rota para adicionar um novo aluno
@app.route('/alunos', methods=['POST'])
def add_aluno():
    novo_aluno = {
        'id': alunos[-1]['id'] + 1,
        'nome': request.json['nome'],
        'idade': request.json['idade'],
        'curso': request.json['curso']
    }
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201

# Rota para atualizar um aluno existente
@app.route('/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    aluno = [aluno for aluno in alunos if aluno['id'] == aluno_id]
    if len(aluno) == 0:
        return jsonify({'mensagem': 'Aluno não encontrado'}), 404
    aluno[0]['nome'] = request.json.get('nome', aluno[0]['nome'])
    aluno[0]['idade'] = request.json.get('idade', aluno[0]['idade'])
    aluno[0]['curso'] = request.json.get('curso', aluno[0]['curso'])
    return jsonify(aluno[0]), 200

# Rota para excluir um aluno
@app.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    aluno = [aluno for aluno in alunos if aluno['id'] == aluno_id]
    if len(aluno) == 0:
        return jsonify({'mensagem': 'Aluno não encontrado'}), 404
    alunos.remove(aluno[0])
    return jsonify({'mensagem': 'Aluno excluído com sucesso'}), 200

if __name__ == '__main__':
    app.run(debug=True)
