from banks_tool import Bank, Account, Account_type



first_bank =Bank("first bank","Commerical","Jos")         
AS_bank = Bank("AS_BANK","MF","ABUJA")

simon =Account(first_bank.name, first_bank.type, "simon", Account_type.save.name, 1000, isAdmin = True, message_type = ["E-MAIL"])
umoru =Account(AS_bank.name, AS_bank.type, "umoru",Account_type.current.name, 2000, isAdmin= False, message_type=["SMS"])
print(simon.deposit(1000))
print(simon.transfer(umoru, 1000))
print(simon.total_transaction)
print(simon.transaction_count)
#print(simon.withdraw(200))
#print(simon.transfer(simon, 800))

print("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*")

print(umoru.total_transaction)
print(umoru.transaction_count)
#print("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*")
print(umoru.domaint())

