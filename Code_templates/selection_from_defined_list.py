import random

diff=["1", "2", "3"]
while True:

    difficulty=(input("Select your difficulty. (between 1-3 with 1 being the easiest): "))
          
    if difficulty not in diff:
            
        continue

    else:

        break

print("you have chosen {} as your difficulty".format(difficulty))
