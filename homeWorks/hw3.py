class Bank:
    def __init__(self, name, balance=0):
        self._name = name
        self._balance = balance

    def __str__(self):
        return f'Name: {self._name}, Balance: {self._balance}\n'

    def moneyX(self):
        amount = float(input("Enter the amount of money to add: "))
        self._balance += amount
        print (f"New balance: {self._balance}")


    def __jackpot(self):
        self._balance *= 10
        print(f"Jackpot! New balance:{self._balance}")

    def _merge_balance(self, other):
        if isinstance(other, Bank):
            self._balance += other._balance
            print(f"Transferred balance from {other._name}. New balance: {self._balance}")
        else:
            print("Transfer failed. The provided object is not a Bank instance.")

    def _kill(self):
        self._balance = 0
        print("Your balance has been reset to zero.")


if __name__ == "__main__":
    bank1 = Bank("Aidai", 100)
    print(bank1)
    bank2 = Bank("Diana", 100)

    bank1.moneyX()
    bank1._Bank__jackpot()
    bank1._merge_balance(bank2)
    bank1._kill()
