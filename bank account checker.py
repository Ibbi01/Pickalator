bank_balance = input("Enter your bank balance: ")
transfer_amount = input("Enter how much you want to transfer: ")
bank_balance=int(bank_balance)
transfer_amount=int(transfer_amount)
if transfer_amount < bank_balance and transfer_amount>0:
   new_balance = bank_balance-transfer_amount
   print("Your new balance is: ",new_balance)
else:
   print("your transaction cannot be made sadly")