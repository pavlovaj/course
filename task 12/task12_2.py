class BankAccount:
    def __init__(self, name, account_number, balance, password):
        self.name = name
        self.account_number = account_number
        self.__balance = balance
        self.__password = password

    def get_balance(self, password):
        if password == self.__password:
            return self.__balance
        else:
            return "Incorrect password."

    def set_balance(self, new_balance, password):
        if password == self.__password:
            self.__balance = new_balance
            return "Balance updated."
        else:
            return "Incorrect password."