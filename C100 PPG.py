print("Welcome to the Emirates NBD Bank ATM portal ")
class atm:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number


    def cashTake(self, card_number):
            print("Money has been successfully taken")
    def balanceEnquiry(self, pin_number):
            print("You have sufficient balance")
            
    def cashDeposit(self, card_number):
            print("Processing, please wait... ")
            print (" ; )")
            print("Your cash is safely deposited")

EmiratesNBDBank = atm(123, 1193)
print(EmiratesNBDBank.cashTake(123))
