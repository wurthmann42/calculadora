def operacoes():
    print("[1] SOMA\n"
          "[2] SUBTRAI\n"
          "[3] MULTIPLICA\n"
          "[4] DIVIDE\n"
          "[5] SAIR")

def numeros_para_int():
    numeros = input("Digite os números separados por vírgula: ")
    numeros_splitado = numeros.split(',')
    numbers = [float(x) if '.' in x else int(x) for x in numeros_splitado]
    return numbers

def opcao():
    opcao = int(input('Digite a sua opção:'))
    return opcao
