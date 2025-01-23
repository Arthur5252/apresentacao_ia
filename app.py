import logging
from flask import Flask, request, send_file, render_template, jsonify
from gerar_conteudo_gpt import *
from criar_apresentacao import *
from separa_topico import *
from helpers import *
import os

# Configurar o logging
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'  # Sobrescreve o arquivo a cada execução
)

app = Flask(__name__)

@app.route('/')
def index():
    app.logger.info("Página inicial acessada.")
    return render_template('index.html') 

@app.route('/frutas', methods=['GET'])
def get_frutas():
    frutas = ['Maçã', 'Banana', 'Laranja', 'Manga', 'Uva']
    app.logger.info("Rota de frutas acessada.")
    return jsonify(frutas)

@app.route('/apps/apresentacao/<int:cod_cliente>', methods=['POST'])
def criar(cod_cliente):
    caminho_base = 'C:/uploads'
    try:
        json_data = request.get_json()
        if not json_data or 'tema' not in json_data:
            app.logger.warning("Requisição sem o campo obrigatório 'tema'.")
            return jsonify({"erro": "Campo 'tema' é obrigatório no corpo da requisição"}), 400

        tema = json_data['tema']
        app.logger.info(f"Tema recebido: {tema}")

        caminho_arquivo = os.path.join(caminho_base, str(cod_cliente), 'slide')
        app.logger.debug(f'Caminho do arquivo: {caminho_arquivo}')

        # Verificar se o diretório existe, se não, criar
        if not os.path.exists(caminho_arquivo):
            os.makedirs(caminho_arquivo)
            app.logger.info(f"Diretório criado: {caminho_arquivo}")
        else:
            app.logger.info("Caminho já existe")

        texto = gerar_conteudo_gpt(prompt=tema)
        topicos = separa_topicos(texto)
        arquivo = criar_apresentacao(topicos, caminho_arquivo, tema)

        app.logger.info(f"Apresentação criada com sucesso: {arquivo}")

        return jsonify({
            "url": f'http://arquivos.octopustax.com.br/{cod_cliente}/slide/{arquivo}',
        }), 200

    except Exception as e:
        app.logger.error(f"Erro ao criar apresentação: {str(e)}")
        return jsonify({"erro": f"Erro ao criar apresentação: {str(e)}"}), 500
if __name__ == '__main__':
    app.run(debug=True)
