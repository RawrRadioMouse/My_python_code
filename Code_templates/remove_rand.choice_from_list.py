import random
random1=["gay","home","bitch-ass","negro","Hoarse-voice","meh","TEST"]


while True:

        name =(input("GIVE ME UR NAME: "))
        if not random1:
            print("list is depleted! you ran through all my options!!!")
            continue
        elif name !=("james"):
            insult=random.choice(random1)
            print("names is james pls not "+name+" not "+insult)
            random1.remove(insult)
            continue

        else:

            print("yes that is correct please proceed")

            break
