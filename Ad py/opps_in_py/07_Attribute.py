class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no= acc_no
        self.__acc_psss= acc_pass
    

    def reset_pass(self):
        print(self.__acc_pass)


acc1= account("123434","asdf") 

print(acc1.acc_no)
print(acc1.reset_pass())