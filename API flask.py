from flask import Flask, jsonify, request

app = Flask(__name__)

viagens = [
    {"id":1, "local": "Destino 1"},
    {"id":2, "local": "Destino 2"},
    {"id":3, "local": "Destino 3"}
]

#Procurar todas as viagens
@app.route('/viagens', methods=['GET'])
def get_viagens():
    return viagens

#Procurar uma viagem especifica por ID
@app.route('/viagens/<int:destino_id>', methods=['GET'])
def get_viagem(destino_id):
    for viagem in viagens:
        if viagem['id']==destino_id:
            return viagem
    return {'error':'Local não encontrado'}

#Criando um cadastro de viagem
@app.route('/viagens', methods=['POST'])
def create_viagem():
    new_viagem={'id':len(viagens)+1, 'local':request.json['local']}
    viagens.append(new_viagem)
    return new_viagem

#Atualizando uma viagem
@app.route('/viagens/<int:destino_id>', methods=['GET'])
def update_viagem(destino_id):
    for viagem in viagens:
        if viagem['id']==destino_id:
            viagem['local']=request.json['local']
            return viagem
        return{'error':'Local não encontrado'}
    
#Deletando uma viagem
@app.route('/viagens/<int:destino_id>', methods=['DELETE'])
def delete_viagem(destino_id):
    for viagem in viagens:
        if viagem['id']==destino_id:
            viagens.remove(viagem)
            return {"data":"Viagem deletada com sucesso"}
        return{'error':'Viagem não encontrada'}
    
#corre o flask
if __name__ =='__main__':
    app.run(debug=True)