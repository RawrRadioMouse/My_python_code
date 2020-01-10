piece_of_garbage=["yes", "no"]
while True:

    garbage=(input("is it a piece of garbage? (select Yes or No): "))
          
    if garbage not in piece_of_garbage:
        print("don't be a piece of garbage, answer the question")    
        continue

    else:

        print("you have said {} ".format(garbage))
        if garbage == "yes":
            print("it is a piece of garbage, now stamp your feet at your standing desk and entertain everyone")
            break
        else:
            print("you are a piece of garbage for lying")
            

