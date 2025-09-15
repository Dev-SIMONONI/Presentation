import random
import datetime 
from enum import Enum
class Bank:
    #class variables
    total_banks=0
    all_banks_names = []
    def __init__(self, bank_name:str, bank_type: str, bank_branch: str="Abuja"):
         self.name:str=bank_name
         self.type:str=bank_type
         self.branches:list[str]=[bank_branch]
         self.customers:int=0
         self.all_account:int=0
         self.all_transactions:list[str]=[]
         Bank.total_banks+=1



            

class Account_type(Enum):
    save ="SAVINGS"
    current="CURRENT"


class Account(Bank):
    transaction_date =datetime.datetime.now()
    def __init__(self, bank_name,bank_type, name: str, types: str, balance: float, isfreeze: bool= False, isAdmin: bool = False, message_type: list=[],  ismessage: bool = True, bank_branch="ABUJA"):
 
        Bank.__init__(self,bank_name,bank_type,bank_branch)
        self.acc_name:str= name
        self.acc_type:str=types
        self.account_number:int=random.randint(1000000000, 9000000000)
        self.total_bal:float=balance
        self.transaction_count:list=0
        self.total_transaction:list=[]
        self.active_notify:bool= ismessage
        self.notify_type= message_type
        self.isAdmin:bool = isAdmin
        self.frozen:bool = isfreeze
        self.Domaint = False
        self.time_keeper = []



    def domaint(self):
        if self.Domaint == False:
            last_transaction = self.time_keeper[-1].date()
            todays = Account.transaction_date.date()
            checker= last_transaction + datetime.timedelta(days=1)
            if checker == todays:
                self.Domaint =True
                return "Account has not been active for 24 Hours"
            else:
                return "Account is active"
        else:
            return "Account is domaint"
            

    def freeze(self):
        if self.isAdmin == True:
            if self.frozen == False:
                self.frozen = True
                return "Your account is currently on frezze no transaction is allowed"

        else:
            return "You do not have access to frezze this account"
        
    def notify(self,trans_type,amount):
        if self.active_notify == True:
            sms=False
            emial=False
            for choice in self.notify_type:
                if choice == "SMS":
                    sms=True
                    print( f"SMS: {trans_type} Alert of {amount} \n Account Name:{self.acc_name}\n Account number:{self.account_number}\n Account Balance: {self.total_bal} \n Transaction date: {self.transaction_date} \n Thank you for banking with us")
                if choice == "E-MAIL":
                    emial=True
                    print (f"E-MAIL {trans_type} Alert of {amount}\n Account Name: {self.acc_name}\n Account number:{self.account_number}\n if you did not approve of this E-Mail send us a message to freeze this account\n Transaction date: {self.transaction_date} \n Thank you for banking with us" )
            return "DONE"


    def deposit(self, amount):
        if self.frozen == True:
            return "Your account is freeze no transaction is premission"
        
        else:
            if amount > 0:
                self.total_bal += amount
                print(self.notify("CREDIT", amount))
                self.transaction_count += 1
                self.time_keeper.append(self.transaction_date)
                self.total_transaction.append(f"CREDIT ALERT Amount:{amount} Transaction details:{self.transaction_date}")
                return f"Current account balance: {self.total_bal}"
            else:
                return "Invalid amount"

    
    def withdraw(self,amount):
       if self.frozen:
            return self.freeze()
       else:
            if amount > 0:
                if amount <= self.total_bal:
                    self.total_bal -= amount
                    print(self.notify("DEBIT ALERT", amount))
                    self.transaction_count += 1
                    self.time_keeper.append(self.transaction_date)
                    self.total_transaction.append(f"DEBIT ALERT Amount:{amount} Transaction details:{self.transaction_date}")


                    return f"Withdraw sucessful"
            
                else:
                    return "Insuffient funds"
            else:
                return "Withdrawal amount must be greater than zero"     


    def transfer(self, recipent, amount):
        if self.frozen == True:
            return self.freeze()
        else:
            if amount <= self.total_bal:
                TF= self.withdraw(amount)
                
                
                if TF == "Withdraw sucessful":
                    
                    recipent.deposit(amount)
                    #self.total_transaction.append(f"DEBIT ALERT:{amount}")
                    
                    print(self.notify("CERDIT ALERT", amount))
                    #recipent.total_transaction.append(f"after deposit function is called i still append to tt list   CREDIT ALERT:{amount}")
                    return "transfer sucessful"
                else:
                    return "withdrawal not sucessful"
            
            else:
                return "Insuffient funds"   







