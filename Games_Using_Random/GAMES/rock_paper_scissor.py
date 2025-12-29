import random
choices=["rock","paper","scissor"]
while True:
    mach_pick=random.choice(choices)
    pick=str(input("Choose one (rock,paper,scissor): "))
    print(mach_pick)
    
    if pick==mach_pick:
        print("IT'S A TIE!!")
        break
    elif mach_pick=="rock" and pick=="paper":
        print("YOU LOST!!")
        break
    elif mach_pick=="paper" and pick=="rock":
        print("CONGO!!! YOU WON!!!!")
        break
    elif mach_pick=="paper" and pick=="scissor":
        print("CONGO!!! YOU WON!!!!")
        break
    elif mach_pick=="scissor" and pick=="paper":
        print("YOU LOST!!")
        break
    elif mach_pick=="scissor" and pick=="rock":
        print("YOU WON!!")
        break
    elif mach_pick=="rock" and pick=="scissor":
        print("YOU LOST!!")
        break
    else:
        print("Wrong choice!! Please try again...")