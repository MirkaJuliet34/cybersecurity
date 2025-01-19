# Você foi encarregado de criar um sistema simples que verifica a integridade de arquivos, comparando o hash fornecido pelo usuário com o hash real do arquivo. 
# Na função verificar_hashes que irá receber uma lista de hashes e compará-los com os valores esperados para cada arquivo. Seu objetivo é verificar se o hash calculado é igual ao hash esperado.

# Entrada
# Uma lista de pares de hashes (hash calculado e hash esperado), separados por vírgulas, e cada par separado por ponto e vírgula.

# Saída
# Para cada par de hashes fornecido, o código imprime o resultado "Correto" ou "Inválido".

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	Saída
# abc123, abc123	Correto
# def456, def789	Inválido
# 123abc, 123abc; 456def,456def	Correto
# Correto

def verificar_hashes(lista_hashes):
    # Para cada par de hashes fornecido na lista
    for hash_comparacao in lista_hashes:
        # Separando o hash calculado e o esperado
        hash_calculado, hash_esperado = hash_comparacao.split(",")
        
        # Remover espaços extras ao redor dos hashes
        hash_calculado = hash_calculado.strip()
        hash_esperado = hash_esperado.strip()
        
        # Verificar se o hash calculado é igual ao esperado
        if hash_calculado == hash_esperado:
            print("Correto")
        else:
            print("Inválido")

# Leitura da entrada
hashes_usuario = input()  # Recebe a entrada de dados do usuário

# Separando as entradas em pares de hashes
lista_hashes = hashes_usuario.split(";")

# Chama a função de verificação com a lista gerada
verificar_hashes(lista_hashes)
