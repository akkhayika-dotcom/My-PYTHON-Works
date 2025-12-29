from check_balance import check_balance
from deposit import deposit
from withdraw import withdraw

balance=100000 

while True:
    print("*******WELCOME*******")
    print("Enter 1 to check balance.")
    print("Enter 2 to deposit money.")
    print("Enter 3 to withdraw money.")
    choose=input("Enter your choice:")
    if choose=="1":
       check_balance(balance)
    elif choose=="2":
      balance=deposit(balance)
    elif choose=="3":
      balance=withdraw(balance)
    else:
        print("Wrong choice!!")
    
