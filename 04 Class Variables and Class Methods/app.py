# Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "HBL"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name 

bank1 = Bank()
bank2 = Bank()

print(bank1.bank_name)
print(bank2.bank_name)

Bank.change_bank_name("MCB")

print(bank1.bank_name)
print(bank2.bank_name)