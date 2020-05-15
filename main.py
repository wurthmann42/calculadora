from calculator import Calculador
from pythonUtils import operacoes, numeros_para_int, opcao

c = Calculador()

while True:
    operacoes()
    try:
        opcao = int(input('Digite a sua opção:'))
    except Exception:
        print("Digite uma opção válida")
        opcao = int(input('Digite a sua opção:'))
    while True:
        if opcao == 1:
            try:
                numeros_inteiros = numeros_para_int()
                print(f"O resultado da soma dos números fornecidos é: {round(c.soma(*numeros_inteiros), 2)}")
                opcao2 = input(f"Fazer outra operação de soma? [S/N]").lower()
                if opcao2 == "n":
                    break
            except Exception as e:
                print(e)
        elif opcao == 2:
            try:
                numeros_inteiros = numeros_para_int()
                print(f"O resultado da subtração dos números fornecidos é: {round(c.subtrai(*numeros_inteiros), 2)}")
                opcao2 = input(f"Fazer outra operação de subtração? [S/N]").lower()
                if opcao2 == "n":
                    break
            except Exception as e:
                print(e)
        elif opcao == 3:
            try:
                numeros_inteiros = numeros_para_int()
                print(f"O resultado da multiplicação dos números fornecidos é: {round(c.multiplica(*numeros_inteiros), 2)}")
                opcao2 = input("Fazer outra operação de multiplicação?").lower()
                if opcao2 == "n":
                    break
            except Exception as e:
                print(e)
        elif opcao == 4:
            try:
                numeros_inteiros = numeros_para_int()
                print(f"O resultado da divisão dos números fornecidos é: {round(c.divide(*numeros_inteiros), 2)}")
                opcao2 = input("Fazer outra operação de divisão?").lower()
                if opcao2 == "n":
                    break
            except Exception as e:
                print(e)
        elif opcao == 5:
            quit()
