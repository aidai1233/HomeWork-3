class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value + other.value)
        return Calculator(self.value + other)

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value - other.value)
        return Calculator(self.value - other)

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value * other.value)
        return Calculator(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value / other.value)
        return Calculator(self.value / other)

    def __repr__(self):
        return f"Calculator({self.value})"

# Пример использования
if __name__ == "__main__":
    calc1 = Calculator(30)
    calc2 = Calculator(40)

    result_add = calc1 + calc2
    result_sub = calc1 - calc2
    result_mul = calc1 * calc2
    result_div = calc1 / calc2

    print(result_add)
    print(result_sub)
    print(result_mul)
    print(result_div)
