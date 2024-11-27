
import random
import string
def gerar_chave():
    def gerar_bloco():
        # Seleciona aleatoriamente 2 letras (maiúsculas) e 3 números
        letras = random.choices(string.ascii_uppercase, k=2)
        numeros = random.choices(string.digits, k=3)
        return ''.join(letras + numeros)
    
    # Gera os três blocos
    bloco1 = gerar_bloco()
    bloco2 = gerar_bloco()
    bloco3 = gerar_bloco()
    
    # Junta os blocos com o separador '-'
    chave = f"{bloco1}-{bloco2}-{bloco3}"
    return chave
def gerar_varias_chaves(quantidade):
    chaves = [gerar_chave() for _ in range(quantidade)]
    return chaves
# Função para salvar as chaves no arquivo "keys.txt"
def salvar_chaves_no_arquivo(chaves):
    with open("keys.txt", "a") as arquivo:  # "a" para adicionar ao arquivo sem sobrescrever
        for chave in chaves:
            arquivo.write(f"{chave}\n")
# Função para perguntar se o usuário quer continuar ou não
def perguntar_continuar():
    resposta = input("Você quer continuar gerando chaves? (S para sim, N para não): ").strip().upper()
    return resposta == "S"
# Loop principal
while True:
    # Solicita ao usuário a quantidade de chaves a ser gerada
    quantidade = int(input("Quantas chaves você deseja gerar? "))
    # Gerar as chaves
    chaves = gerar_varias_chaves(quantidade)
    # Exibe as chaves geradas
    for chave in chaves:
        print(chave)
    # Salva as chaves no arquivo
    salvar_chaves_no_arquivo(chaves)
    # Pergunta se o usuário quer continuar
    if not perguntar_continuar():
        print("Programa encerrado.")
        break
# Espera o usuário pressionar Enter antes de fechar
input("Pressione Enter para sair...")```
