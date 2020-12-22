class Calculador:
    def soma(self, *args):
        res = 0
        for numbers in args:
            res += numbers
        return res

    def subtrai(self, *args):
        res = args[0]
        for numbers in args[1:]:
            res -= numbers
        return res

    def multiplica(self, *args):
        res = 1
        for numbers in args:
            res *= numbers
        return res

    def divide(self, *args):
        res = args[0]
        for numbers in args[1:]:
            if numbers == 0:
                return "Not a number"
            res /= numbers
        return res
