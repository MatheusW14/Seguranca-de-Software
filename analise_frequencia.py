def contar_letras(texto):
    """Conta e exibe frequência das letras do texto dado."""
    contagem = {}

    for letra in texto:
        if letra.isalpha():
            contagem[letra] = contagem.get(letra, 0) + 1

    letras_ordenadas = sorted(contagem.items(), key=lambda item: (-item[1], item[0]))

    print("\n📊 CONTAGEM DE LETRAS (atualizada):")
    print("-----------------------------------")
    print(" Letra | Quantidade ")
    print("-----------------------------------")
    for letra, quantidade in letras_ordenadas:
        print(f"   {letra}   |     {quantidade}")
    print("-----------------------------------")


def substituir_letras_em_loop(texto):
    """Permite substituir letras no texto diretamente, com contagem atualizada."""
    texto_modificado = texto
    historico = [texto_modificado]

    while True:
        print("\n--- TEXTO ATUAL ---")
        print(texto_modificado)

        print("\nOpções:")
        print("  [S] Substituir letra")
        print("  [D] Desfazer substituição")
        print("  [N] Sair")
        opcao = input("Escolha uma opção: ").strip().lower()

        if opcao == "n":
            print("\n✅ Texto final:", texto_modificado)
            break

        elif opcao == "d":
            if len(historico) > 1:
                historico.pop()
                texto_modificado = historico[-1]
                print("↩️ Substituição desfeita.")
            else:
                print("⚠️ Nada para desfazer.")

        elif opcao == "s":
            letra_original = input("Letra a substituir: ").lower()
            letra_nova = input(f"Substituir '{letra_original}' por: ").lower()

            if not (letra_original.isalpha() and len(letra_original) == 1):
                print("❌ Insira apenas UMA letra válida.")
                continue
            if not (letra_nova.isalpha() and len(letra_nova) == 1):
                print("❌ Insira apenas UMA letra válida.")
                continue
            if letra_original not in texto_modificado:
                print(f"⚠️ A letra '{letra_original}' não está presente.")
                continue

            texto_modificado = texto_modificado.replace(letra_original, letra_nova)
            historico.append(texto_modificado)

            print(f"\n🔄 Texto atualizado: {texto_modificado}")
        else:
            print("❌ Opção inválida.")

        # Mostrar contagem após cada ação
        contar_letras(texto_modificado)


def main():
    print("\n=== CONTADOR E SUBSTITUIDOR DE LETRAS ===")
    texto = """Urtklm tr dqapuakcftr ltr iasqtr aj nmqsuouar lacfdqa t jakrtoaj tetfxm acmjniasa t steait ntqt qaofrsqtq tr ruersfsufcmar akcmksqtltr""".lower()
    contar_letras(texto)
    substituir_letras_em_loop(texto)


if __name__ == "__main__":
    main()
