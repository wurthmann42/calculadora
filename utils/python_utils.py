class Utils:

    @staticmethod
    def display_operations():
        print("[1] SOMA\n" "[2] SUBTRAI\n" "[3] MULTIPLICA\n" "[4] DIVIDE\n" "[5] SAIR")

    @staticmethod
    def numeros_para_int():
        try:
            numeros = input("Digite os números separados por vírgula: ")
            numeros_splitado = numeros.split(",")
            numbers = [float(x) if "." in x else int(x) for x in numeros_splitado]
            return numbers
        except Exception as e:
            print("Ops! Voce digitou errado... Digite novamente: ")

