from Sci_calc.add import addition
from Sci_calc.subtraction import subtract
from Sci_calc.multiply import multiply
from Sci_calc.division import division
from Sci_calc.modulus import mod
from Sci_calc.expo import expo



def calc(x,y,operations):
    if operations=="+":
        ans = addition(x,y)
    elif operations=="-":
        ans = subtract(x,y)
    elif operations=="*":
        ans = multiply(x,y)
    elif operations=="/":
        ans = division(x,y)
    elif operations=="%":
        ans = mod(x,y)
    elif operations=="**":
        ans = expo(x,y)
    else:
        print("INCORRECT OPERATOR!")
    return ans
    
while True:
    print("******WELCOME******")
    x=float(input("Enter the first number:"))
    y=float(input("Enter the second number:"))
    print("For summation press----> +")
    print("For subtraction press----> -")
    print("For multiplication press----> *")
    print("For division press----> /")
    print("For modulus press----> %")
    print("For exponential press----> **")
    operations=str(input("Enter your operand:"))

    ans=calc(x,y,operations)
   
    print("ANSWER:",ans)
    