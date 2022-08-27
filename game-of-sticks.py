"""
- There are 21 sticks
- First user picks sticks between 1-4
- Computer picks (1-4)

*challenge*
- whoever picks last stick looses

"""

sticks = 21


while True:
    sticks_taken = int(input("Take sticks (1-4): "))
    if sticks == 1:
        print("you took last stick, you are looser")
        break

    if sticks_taken >= 5 or sticks_taken <= 0:
        print("wrong choice")
        continue

    print("computer took: ", (5-sticks_taken), "\n")
    sticks = sticks - 5

