
# Apresentação IA
Programa que cria uma apresentação a partir de um tema digitado pelo usuário, gerando um "roteiro" da apresentação e criando uma apresentação com um template pré-definido.

# Fluxo
Front-end faz uma requisição POST para a rota /criar, enviando um JSON com o tema da apresentação.
A rota ativa as funções que compõem o programa.

A primeira função envia o tema da apresentação como prompt para a OpenAI, junto com um modelo de estrutura para a apresentação. A OpenAI retorna a estrutura de apresentação de acordo com o tema escolhido.

A resposta da OpenAI é uma string longa, então é necessário separar os tópicos para que cada tópico ocupe um slide.

Após isso, o arquivo pptx é montado utilizando como template o arquivo modelo_octopus.pptx. O arquivo é salvo.

Enviamos o arquivo de volta para o Front-end utilizando mimetype='application/vnd.openxmlformats-officedocument.presentationml.presentation'.
