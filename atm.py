import time

class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.balance = 1000

    def cashWithdrawal(self):
        print("Your balance is:", self.balance)
        moneyToWithdraw = input("Enter amount of money to withdraw: ")
        checkCN = input("Enter your card number: ")
        checkPN = input("Enter your PIN: ")
        # print(checkCN, self.cardnumber, checkPN, self.pin) debugging
        if int(checkCN) == self.cardnumber and int(checkPN) == self.pin:
            if int(moneyToWithdraw) <= self.balance:
                self.balance -= int(moneyToWithdraw)
                print("Successfully withdrew " + str(moneyToWithdraw) + " dollars!")
                print("New balance:", self.balance)
                print("Thank you for using this ATM!")
                quit()
            else:
                print("Insufficient balance!")
                time.sleep(3)
                self.start()
        else:
            print("Invalid Card Number or PIN, please try again.")
            time.sleep(3)
            self.start()

    def checkBal(self):
        print("Your balance is:", self.balance)
        time.sleep(3)
        self.start()

    def start(self):
        print("Welcome to the ATM! What would you like to do today?")
        print("1: Withdraw Money")
        print("2: Check Balance")
        print("3: End session")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            self.cashWithdrawal()
        elif choice == "2":
            self.checkBal()
        elif choice == "3":
            print("Thank you for using this ATM!")
            time.sleep(2)
            quit()
        else:
            print("Please enter a valid choice (1, 2, or 3).")
            time.sleep(3)
            self.start()

new_user = Atm(cardnumber="123456789", pin="1234")
new_user.start()