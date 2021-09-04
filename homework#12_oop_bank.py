#Ashat_Polvanov

# Создайте класс BankAccount, который представляет банковский счет, c атрибутами экземпляра: 
# accountNumber (числовой тип), name (имя владельца счета строкового типа), balance.
# Создайте конструктор с параметрами: accountNumber, name, balance.
# Создайте метод Deposit(), который управляет действиями по пополнению счета.
# Создайте метод Withdrawal(), который управляет действиями по снятию средств.
# Создайте метод bankFees() для применения банковской комиссии в размере 5% от баланса счета.
# Создайте метод display() для отображения деталей счета.
# Приведите примеры использования.



class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def get_deposit(self, refill_amount):
        self.balance += refill_amount
        print(self.balance)   # для проверки

    def withdrawal(self, ammount):
        if self.balance > ammount:
            self.balance = self.balance - ammount
            print(self.balance)    # для проверки
        else:
            print('''Недостаточно средств для снятия!
Ваш баланс: {}'''.format(self.balance))

    def take_away_bank_fees(self, bank_fees = 0):
        bank_fees = self.balance / 100 * 5
        self.balance -= bank_fees
        print(self.balance, bank_fees)   # для проверки

    def view_information(my_account):
        print('ID | NAME | BALANCE')
        print(my_account.account_number , ' | ',my_account.name + ' | ' , my_account.balance)
    

my_account = BankAccount(1, 'Test', 1000)
my_account.view_information()
my_account.get_deposit(500)
my_account.withdrawal(550)
my_account.take_away_bank_fees()
my_account.view_information()
