from openai import OpenAI
from helpers import *

modelo = carrega('modelo_apresentacao.txt')

#client = OpenAI(api_key='Chave API AQUI')

def gerar_conteudo_gpt(prompt):
    try:
        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": 
            f"Você atuará como uma ferramenta de criação de apresentação, voce recebera um prompt e a partir deste prompt voce vai criar uma apresentação de power point. A sua resposta será renderizada em um slide, então evite usar formatação markdown. Nas suas respostas não inclua indicativos dos slides como por exemplo: 'Slide 1: ,Slide 2:' etc. Utilize como exemplo para criar suas apresentações o seguinte modelo: {modelo}"},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
        # Retornar o conteúdo gerado
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Erro ao chamar a API: {e}")
        return None  # Retornando None em caso de erro