class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no= acc
    #debit method

    def debit(self,amout):
        self.balance -=amout
        print("Rs",amout, "was debited")
        print("total balance is =",self.get_balance())


    def credit(self,amout):
        self.balance+=amout
        print("Rs",amout,"was creadited")    
        print("total balance is =",self.get_balance())

    def get_balance(self):
        return self.balance    



acc1 = Account(10000,12345)
print(acc1.balance)
print(acc1.account_no)  
acc1.debit(1000)  
acc1.credit(500)
