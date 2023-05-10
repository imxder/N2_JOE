from flask import Flask, request, jsonify

app = Flask(__name__)

materiais = []
quantidades = []

@app.route('/materiais', methods=['GET'])
def pegar_materiais():
    dados_materiais = []
    for i, material in enumerate(materiais):
        dados_material = {
            'id': i,
            'name': material,
            'qtde': quantidades[i]
        }
        dados_materiais.append(dados_material)
    response = jsonify({'materiais': dados_materiais}), 200
    return response

@app.route('/materiais', methods=['POST'])
def criar_material():
    data = request.json
    material = data['material']
    nome = material['name']
    qtde = material['qtde']
    materiais.append(nome)
    quantidades.append(qtde)
    response = jsonify({'mensagem': f'{nome} criado com sucesso!'}), 201
    return response

@app.route('/materiais/<int:id>', methods=['GET'])
def buscar_material_por_id(id):
    if id < len(materiais):
        nome = materiais[id]
        qtde = quantidades[id]
        material = {
            'id': id,
            'name': nome,
            'qtde': qtde
        }
        response = jsonify({'material': material}), 200
        return response
    else:
        response = jsonify({'mensagem': f'Material com ID {id} não encontrado.'}), 404
        return response
    
@app.route('/materiais/<int:id>', methods=['PUT'])
def atualizar_material(id):
    if id < len(materiais):
        material = request.json['material']
        materiais[id] = material['name']
        quantidades[id] = material['qtde']
        response = jsonify({'mensagem': f'{material["name"]} atualizado com sucesso!'}), 200
        return response
    else:
        response = jsonify({'mensagem': f'Material com ID {id} não encontrado.'}), 404
        return response
    
@app.route('/materiais/<int:id>', methods=['DELETE'])
def remover_material(id):
    if id < len(materiais):
        del materiais[id]
        del quantidades[id]
        response = jsonify({'materiais': materiais}), 200
        return response
    else:
        response = jsonify({'mensagem': f'Material com ID {id} não encontrado.'}), 404
        return response


if __name__ == '__main__':
    app.run(host="localhost", port="5000", debug=True)
