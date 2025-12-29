def deposit(balance):
   deposit_amount=int(input("Enter your deposit amount:"))
   new_balance=balance+deposit_amount
   print(f"\n{deposit_amount} has been successfully deposited.New balance is {new_balance}")
   return new_balance

