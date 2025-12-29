import random
import time
future=["✨ Yes! Absolutely! ✨","🌙 No, not in your stars 🌙","💫 Maybe… only time will tell 💫","🌜 Possibly… under the moonlight 🌜","🌞 The universe is working behind the curtain 🌞","💭 I don't think so 💭"," 🌸 You'll have to wait 🌸 "]

while True:
    print(".....HI!! THIS IS CHIM, A MAGIC BALL THAT CAN SEE YOUR FUTURE.....")
    question=input("What do you want to know about your future?---")
    time.sleep(2)
    print("Calculating the stars💫....")
    time.sleep(3)
    magic_guess=random.choice(future)
    print(magic_guess)