def valid_nif(nif):
    if len(nif) != 9:
        print("NIF inválido")
        return False
    else:
        soma = 0
        for i in range(8):
            soma += int(nif[i]) * (9-i)
        resultado = soma % 11
        digito_controlo = 0 if resultado < 2 else 11 - resultado
        if int(nif[8]) == digito_controlo:
            print("NIF válido")
            return True
        else:
            if '8' in nif:
                print("Tentativa de corrigir: Substituir 8 por 0")
                nif_corrigido = nif.replace('8', '0')
                return print(nif_corrigido)
            else:
                print("Nenhum 8 encontrado para corrigir")
                return nif

valid_nif("584798171")


