class Atm:

    # Class variable
    __counter = 1
    def __init__(self):

        #instance variable
        self.__pin =1234
        self.__balance = 50000
        self.sl = Atm.__counter
        Atm.__counter = Atm.__counter + 1
        #self.__menu()
    
    def __menu(self):
        user_input = int(input("""
                           What's on your mind?
                           1. Change pin
                           2. Deposit
                           3. Widthdraw
                           4. Check balance
                           5. Exit
                               
"""))
        if user_input ==1:
            self.change_pin()
        elif user_input == 2:
            self.deposit()
        elif user_input == 3:
            self.withdraw()
        elif user_input == 4:
            self.check_balance()
        elif user_input == 5:
            print("Thank you for using our system")
        else:
            print("Invalid Input")
            self.__menu()

    def check_pin(self):
        temp = int(input("Enter your pin: "))
        if self.__pin == temp:
            return True
        else:
            return False

    def change_pin(self):
        if(self.check_pin()):
            temp2 = int(input("Enter a new pin: "))
            self.__pin = temp2
            print("Print created successfully")
        else:
            print("Invalid Pin")
        self.__menu()

    def deposit(self):
        if (self.check_pin()):
            amount = int(input("Enter deposit amount: "))
            self.__balance += amount
            print(f"Deposit Successfull and your current balance is {self.__balance} ")
        else:
            print("Invalid Pin")
        self.__menu()

    def withdraw(self):
        if (self.check_pin()):
            amount = int(input("Enter the withrawal amount: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrawal successful and your current balance is {self.__balance}")
            else:
                print("Insufficient amount")
        else:
            print("Invalid pin")
        self.__menu()
    
    def check_balance(self):
        if(self.check_pin()):
            print(f"Your current balance is {self.__balance}")
        else:
            print("Invalid pin")
        self.__menu()        
        

        