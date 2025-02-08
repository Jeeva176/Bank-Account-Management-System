class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,amnt,name):
        self.amnt=amnt
        self.name=name
        print(f"\n Account '{self.name}' Created.\n Balance=$ '{self.amnt}' ")

    def get_balance(self):
        print(f"\n Account '{self.name}' Balance=$ '{self.amnt}' ")   

# send money at time other  person money

    def deposit(self,amnt):
        self.amnt=self.amnt+amnt
        print(f'\n DEPOSIT COMPLETED')
        self.get_balance()

# send money at time there should money

    def viable_transaction(self,amnt):
        if self.amnt>=amnt:
            return
        else:
            raise BalanceException(f"\n sorry account is '{self.name}' only has a balance of $ '{self.amnt}' ")
        

    def withdraw(self,amnt):
        try:
            self.viable_transaction(amnt)
            self.amnt=self.amnt-amnt
            print('\n Withdraw Completed.')
            self.get_balance()
        except BalanceException as error:
            print(f'\n Withdraw Interrupted ')    


    def transfer(self,amnt,acc):
        try:
            print(f'\n Begin Transfer')
            self.viable_transaction(amnt)
            self.withdraw(amnt)    
            acc.deposit(amnt)
            print("Transfer Completed")
        except BalanceException as error:
            print(f"\n Transfer Interrupted.{error}")             

class InterestRewardAccount(BankAccount):
    def deposit(self,amnt):
        Total=amnt*1.05
        self.amnt+=Total  
        print(f'\n Deposit Complete')
        self.get_balance()

class SavingAcct(InterestRewardAccount):
    def __init__(self,amnt,name):
        super().__init__(amnt,name)
        print(f'\n saving account created"{self.amnt}" with innitial balance "{self.name}" ')
        self.fee=5

    def withdraw(self,amnt):
        try:
            total_amount = amnt + self.fee
            print(f"Attempting to withdraw ${total_amount} from {self.name}")
            self.viable_transaction(total_amount)
            self.amnt -= total_amount
            print(f'\nWITHDRAWAL COMPLETED ')
            self.get_balance()
        except BalanceException as error:
            print(f'\nWITHDRAWAL INTERRUPTED: {error}')

bala=BankAccount(1000,'jeev')
delli=BankAccount(2000,'babu')

bala.get_balance()  
delli.get_balance()


bala.deposit(10)    
delli.deposit(50)

bala.withdraw(500)
delli.viable_transaction(300) 

bala.transfer(200,delli)

Mani=InterestRewardAccount(3000,'JEEVA')
Mani.get_balance()
Mani.deposit(200)

kani=SavingAcct(400,'babu')
kani.get_balance()
kani.deposit(20)
kani.transfer(40,Mani)