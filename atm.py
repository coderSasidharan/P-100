class Atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def check_balance(self):
        print("Your balance is 100")

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
    Card_number = input("enter your card number:- ")
    pin_number  = input("enter your pin number:- ")

    user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        user.withdrawl(amount)
    else:
        print("enter a valid number")

main()