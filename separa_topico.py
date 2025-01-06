def separa_topicos(texto):
    topicos_dict = {}  # Inicializa um dicionário vazio para armazenar os tópicos
    topicos = texto.strip().split('\n\n')  # Divide o texto em blocos (títulos)
    
    for topico in topicos:
        partes = topico.split(':', 1)  # Divide no primeiro ':'
        if len(partes) == 2:  # Verifica se há título e conteúdo
            titulo = partes[0].strip()  # Título (parte antes dos dois pontos)
            conteudo = partes[1].strip()  # Conteúdo (parte depois dos dois pontos)

            subticos_dict = {}  # Inicializa o dicionário para os subtópicos
            linhas = conteudo.split('\n')  # Divide o conteúdo em linhas

            subtitulo_atual = None  # Variável para armazenar o subtítulo atual

            for linha in linhas:
                linha = linha.strip()  # Remove espaços em branco de ambos os lados
                
                if linha.startswith('- '):  # Verifica se a linha é um subtítulo
                    subtitulo_atual = linha[2:].strip()  # Remove '- ' e armazena o subtítulo no ativo
                    subticos_dict[subtitulo_atual] = []  # Inicializa uma lista para armazenar os conteúdos desse subtítulo
                    
                elif linha.startswith('* ') and subtitulo_atual:  # Verifica se a linha é conteúdo de um subtítulo
                    conteudo_sub = linha[2:].strip()  # Remove '* ' e armazena o conteúdo
                    subticos_dict[subtitulo_atual].append(conteudo_sub)  # Adiciona o conteúdo à lista do subtítulo

            # Converte as listas de conteúdos em strings (juntando com ' ' se houver mais de um)
            for s in subticos_dict:
                subticos_dict[s] = ' '.join(subticos_dict[s])  # Junta os conteúdos em uma única string, se houver mais de um

            topicos_dict[titulo] = subticos_dict  # Adiciona o dicionário de subtópicos ao título

    return topicos_dict  # Retorna o dicionário com os tópicos e subtópicos
