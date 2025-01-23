from flask import Flask, request, send_file, render_template, jsonify
from gerar_conteudo_gpt import *
from criar_apresentacao import *
from separa_topico import *
from helpers import *

app = Flask(__name__)

# Rota para a página principal
@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/frutas', methods=['GET'])
def get_frutas():
    frutas = ['Maçã', 'Banana', 'Laranja', 'Manga', 'Uva']
    app.logger.info("Rota de frutas acessada.")
    return jsonify(frutas)

# Rota para gerar a apresentação
@app.route('/criar', methods=['POST'])
def criar():
    tema = request.get_json['tema']
    texto = gerar_conteudo_gpt(prompt=tema)
    topicos = separa_topicos(texto)  # Separa os tópicos
    arquivo = criar_apresentacao(topicos)  # Cria a apresentação
    return send_file(arquivo, as_attachment=True, download_name='apresentacao.pptx', mimetype='application/vnd.openxmlformats-officedocument.presentationml.presentation')  # Retorna o arquivo para download

if __name__ == '__main__':
    app.run(debug=True)
