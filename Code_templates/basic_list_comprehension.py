#below code will print out every possible combinations of coordinates to a cuboid or some shit, I dunno exactly what the purpose is and this challenge was trash
if __name__ == '__main__':
    x = int(1)
    y = int(1)
    z = int(2)
    n = int(3)

    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if n != sum([i,j,k])])

#below code will create a list itemising each iteration in the string,
#giving an output of ['h', 'u', 'm', 'a', 'n']
test=("human")
h_letters = [ i for i in test]
print( h_letters)

#below code will create a list itemising each iteration in the string,
# as long as the iteration is "h", giving an obvious output of "h"
test=("human")
h_letters = [ i for i in test if i == "h"]
print( h_letters)


#Conditionals in List Comprehension
#we create a list based upon the conditions we set it - in this case we build a list
#by checking that each iteration of range20 (1-19) can be divided by 2
number_list = [ i for i in range(20) if i % 2 == 0]
print(number_list)

#nested if in list comprehension
#here we simply add another if clause, now the iteration must be able to be divided
#by 2 and then dividied by 5, thus giving us each multiple of 10 (excluding 100 as range
#function does not count the end) [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
num_list = [i for i in range(100) if i % 2 == 0 if i % 5 == 0]
print(num_list)

