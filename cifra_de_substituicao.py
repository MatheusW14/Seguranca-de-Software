import string
from collections import Counter

# Alfabeto padrão
ALFABETO = string.ascii_lowercase
TAMANHO_ALFABETO = len(ALFABETO)

# Chave fixa padrão (substituição reversa)
CHAVE_FIXA = "zyxwvutsrqponmlkjihgfedcba"


# 1. Função de criptografia
def criptografar(texto_claro: str, chave_cript: str = CHAVE_FIXA) -> str:
    """
    Criptografa um texto usando cifra de substituição.
    Chave deve conter 26 caracteres únicos.
    Mantém maiúsculas/minúsculas e caracteres não alfabéticos.
    """
    chave_cript = chave_cript.lower()
    if (
        len(set(chave_cript)) != TAMANHO_ALFABETO
        or len(chave_cript) != TAMANHO_ALFABETO
    ):
        raise ValueError("Chave inválida! Deve conter 26 caracteres únicos.")

    mapeamento = {}
    for letra_original, letra_chave in zip(ALFABETO, chave_cript):
        # Mapeia minúsculas e maiúsculas
        mapeamento[letra_original] = letra_chave.lower()
        mapeamento[letra_original.upper()] = letra_chave.upper()

    return "".join(mapeamento.get(c, c) for c in texto_claro)


# 2. Função de descriptografia
def descriptografar(texto_cifrado: str, chave_descript: str) -> str:
    """
    Descriptografa um texto usando a chave fornecida.
    """
    chave_descript = chave_descript.lower()
    mapeamento_inverso = {}
    for letra_original, letra_chave in zip(ALFABETO, chave_descript):
        mapeamento_inverso[letra_chave.lower()] = letra_original.lower()
        mapeamento_inverso[letra_chave.upper()] = letra_original.upper()

    return "".join(mapeamento_inverso.get(c, c) for c in texto_cifrado)


# 3. Função de análise de frequência (opcional)
def analisar_frequencia(texto_cifrado: str) -> str:
    """
    Tenta decifrar usando análise de frequência do português.
    Retorna uma possível decifração.
    """
    # Frequência típica das letras em português (ordem decrescente)
    FREQ_PORTUGUES = "aeosridmnutclpvhgqbfzjxkw"

    # Contar frequência das letras no texto cifrado
    contagem = Counter(c.lower() for c in texto_cifrado if c.isalpha())
    letras_ordenadas = [letra for letra, _ in contagem.most_common()]

    # Criar mapeamento provável
    mapeamento = {}
    for cifrada, original in zip(letras_ordenadas, FREQ_PORTUGUES):
        mapeamento[cifrada] = original

    # Aplicar substituição
    texto_decifrado = []
    for c in texto_cifrado:
        if c.lower() in mapeamento:
            substituto = mapeamento[c.lower()]
            texto_decifrado.append(substituto.upper() if c.isupper() else substituto)
        else:
            texto_decifrado.append(c)

    return "".join(texto_decifrado)


# Interface com o usuário
if __name__ == "__main__":
    print("Cifra de Substituição")
    print("1. Criptografar texto")
    print("2. Descriptografar texto")
    print("3. Tentar decifrar com análise de frequência (experimental)")

    opcao = input("Escolha uma opção (1/2/3): ")

    if opcao == "1":
        texto = input("Texto claro: ")
        chave = input("Chave (deixe em branco para chave fixa): ")
        if not chave:
            chave = CHAVE_FIXA
        print("Texto cifrado:", criptografar(texto, chave))

    elif opcao == "2":
        texto = input("Texto cifrado: ")
        chave = input("Chave: ")
        print("Texto decifrado:", descriptografar(texto, chave))

    elif opcao == "3":
        texto = input("Texto cifrado: ")
        print("\nTentativa de decifração por frequência:")
        print(analisar_frequencia(texto))
        print("\nAviso: Resultado pode não ser preciso!")

    else:
        print("Opção inválida!")
