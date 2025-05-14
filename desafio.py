def get_column_order(key):
    """Retorna a ordem das colunas baseada na chave."""
    sorted_pairs = sorted(
        [(char, idx) for idx, char in enumerate(key)], key=lambda x: (x[0], x[1])
    )
    return [idx for char, idx in sorted_pairs]


def get_inverse_permutation(permutation):
    """Retorna a permutação inversa para descriptografia."""
    inverse = [0] * len(permutation)
    for i, j in enumerate(permutation):
        inverse[j] = i
    return inverse


def encrypt_transposition(plaintext, key):
    """Criptografa texto usando cifra de transposição."""
    plaintext = "".join(filter(str.isalpha, plaintext.upper()))
    key = key.upper()
    key_length = len(key)

    if key_length == 0:
        raise ValueError("A chave não pode ser vazia")

    # Adiciona padding com 'X' se necessário
    pad_length = (key_length - (len(plaintext) % key_length)) % key_length
    padded_text = plaintext + "X" * pad_length

    # Cria matriz e lê colunas na ordem definida pela chave
    num_rows = len(padded_text) // key_length
    matrix = [
        list(padded_text[i * key_length : (i + 1) * key_length])
        for i in range(num_rows)
    ]
    column_order = get_column_order(key)

    ciphertext = "".join(
        [matrix[row][col] for col in column_order for row in range(num_rows)]
    )
    return ciphertext


def decrypt_transposition(ciphertext, key):
    """Descriptografa texto cifrado com transposição."""
    ciphertext = "".join(filter(str.isalpha, ciphertext.upper()))
    key = key.upper()
    key_length = len(key)

    if key_length == 0:
        raise ValueError("A chave não pode ser vazia")
    if len(ciphertext) % key_length != 0:
        raise ValueError(
            "O texto cifrado deve ter tamanho múltiplo do tamanho da chave"
        )

    # Divide o texto cifrado em colunas e reordena
    num_rows = len(ciphertext) // key_length
    column_order = get_column_order(key)
    inverse_order = get_inverse_permutation(column_order)

    # Reconstrói a matriz original
    encrypted_columns = [
        ciphertext[i * num_rows : (i + 1) * num_rows] for i in range(key_length)
    ]
    original_columns = [encrypted_columns[i] for i in inverse_order]

    # Lê a matriz linha por linha
    decrypted = "".join(
        "".join([col[row] for col in original_columns if row < len(col)])
        for row in range(num_rows)
    ).rstrip("X")

    return decrypted


def main():
    print("Cifra de Transposição")
    print("1. Criptografar")
    print("2. Descriptografar")
    opcao = input("Escolha (1/2): ")

    if opcao == "1":
        texto = input("Texto claro: ")
        chave = input("Chave (ex: 'MEGABUCK'): ").strip().upper()
        try:
            cifrado = encrypt_transposition(texto, chave)
            print("\nTexto cifrado:", cifrado)
        except ValueError as e:
            print("Erro:", e)

    elif opcao == "2":
        texto_cifrado = input("Texto cifrado: ")
        chave = input("Chave: ").strip().upper()
        try:
            decifrado = decrypt_transposition(texto_cifrado, chave)
            print("\nTexto decifrado:", decifrado)
        except ValueError as e:
            print("Erro:", e)

    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()
