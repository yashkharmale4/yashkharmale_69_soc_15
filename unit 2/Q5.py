class bank:
    def __init__(self,accountno,blance=0):
        self.accountno=accountno
        self.blance=blance

    def deposit(self,amount):
        self.amount=amount

        if amount>0:
            self.blance+=amount

            print(f"Deposited:Rs.{amount}")
        else:
            print(f"Deposit amount must be greater than zero.") 

    def widrawal(self,amount):

        self.amount=amount
        if 0<amount<self.blance  : 
             self.blance-=amount
             print(f"Withdrawn:Rs.{amount}")
        elif amount > self.balance:
            print(f"Insufficient Balance!")

    def check(self):
        print("your blance is ",self.blance)

a=bank(23,500)
a.deposit(500)
a.widrawal(500)
a.check()