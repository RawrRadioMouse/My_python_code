line = ("this is a string")
def split_and_join(line):
    #the below code converts a string into a list, we tell it that we "split" the string off at each " " (space"
    line=line.split(" ")
    #the below line of code puts the string back together, joining all the splits with a "-"
    line="-".join(line)
    return

result = split_and_join(line)
    print result

