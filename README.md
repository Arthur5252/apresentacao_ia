# apresentacao_ia
Programa que cria uma apresentação a partir de um tema digitado pelo usuário, gerando um "roteiro" da apresentação e criando uma apresentação com um template pre definido.

# Fluxo
1 - Front-end faz un request POST para a rota /criar enviando um json com o tema da apresentação.
A rota ativa as funções que compoe o programa.

2 - primeira função envia o tema da apresentação como prompt para a OpenAI junto com um modelo de estrutura para a apresentação. A OpenAI retorna a estrutura de apresentação de acordo com o tema escolhido.

3 - A resposta da OpenAI é uma String longa, então é necessario separar os topicos para que cada tópico ocupe um slide.

4 - Apos isso o arquivo pptx é montado utilizando como template o arquivo modelo_octopus.pptx. O arquivo é salvo.

5 - Enviamos o arquivo de volta para o Front-end utilizando mimetype='application/vnd.openxmlformats-officedocument.presentationml.presentation').
