def withdraw(balance):
    withdraw_amount=float(input("Enter the amount to be withdraw:"))
    if withdraw_amount<=balance:
        print("\nYour transaction is being processed.")
        balance_after_withdrawl=balance- withdraw_amount
        print(f"{withdraw_amount} has been debited.")
        return balance_after_withdrawl
    else:
        print("\nInsufficient balance!")   
        return balance