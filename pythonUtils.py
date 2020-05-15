def operacoes():
    print("[1] SOMA\n"
          "[2] SUBTRAI\n"
          "[3] MULTIPLICA\n"
          "[4] DIVIDE\n"
          "[5] SAIR")

def numeros_para_int():
    numeros = input("Digite os números separados por vírgula: ")
    numeros_splitado = numeros.split(',')
    numeros_inteiros = tuple(map(int, numeros_splitado))
    return numeros_inteiros

def opcao():
    opcao = int(input('Digite a sua opção:'))
    return opcao
