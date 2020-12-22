from utils.python_utils import Utils as utils

class Calculador:

    def operator(self, operation):
        method = getattr(self, operation)
        if operation != "exit":
            numeros_inteiros = utils.numeros_para_int()
            return method(*numeros_inteiros)
        return method()

    def soma(self, *args):
        res = 0
        for numbers in args:
            res += numbers
        return round(res, 2)

    def subtracao(self, *args):
        res = args[0]
        for numbers in args[1:]:
            res -= numbers
        return round(res, 2)

    def multiplicacao(self, *args):
        res = 1
        for numbers in args:
            res *= numbers
        return round(res, 2)

    def divisao(self, *args):
        res = args[0]
        for numbers in args[1:]:
            if numbers == 0:
                return "Divisão por 0 não permitida!"
            res /= numbers
        return round(res, 2)

    def exit(self):
        quit()
