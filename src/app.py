from calculator import Calculador
from utils.python_utils import Utils as utils

OPERATION_TYPE={
        1: "soma",
        2: "subtracao",
        3: "multiplicacao",
        4: "divisao",
        5: "exit"
        }

calc = Calculador()

def main():
    while True:
        utils.operacoes()

        try:
            opcao = int(input("Digite a sua opçào: "))
        except Exception as e:
            print("Opção invalida")
            opcao = int(input("Digite a sua opção: "))

        operacao = OPERATION_TYPE.get(opcao)

        while True:
            try:
                #numeros_inteiros = utils.numeros_para_int()
                print(f"O resultado da operação é: {calc.operator(operacao)}")
                segunda_opcao = input(f"Fazer outra operação? [S/N]").lower()

                while segunda_opcao not in "sn":
                    print("Opção inválida")
                    segunda_opcao = input("Fazer outra operação? [S/N]").lower()
                if segunda_opcao == "n":
                    break
            except Exception as e:
                print(e)

if __name__ == "__main__":
    main()
