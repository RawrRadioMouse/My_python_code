#Given list is ["2","3","6","6","5"]. The maximum score is 6 , second maximum is5 . Hence, we print  as the runner-up score.


if __name__ == '__main__':
    n = int(input())
    #HERE WE MODIFY THE EXAMPLE CODE TO MAKE arr A LIST SO WE CAN USE SORT AND REMOVE FUNCTION
    arr = list(map(int, input().split()))
#HERE WE SET A VARIABLE TO BE THE CURRENT MAX OF LIST, THEN WE SAY "AS LONG AS THE MAXIMUM NUMBER IN LIST IS THE SAME AS STORED MAX, REMOVE IT FROM LIST" DOING THIS ENSURES THAT WE WILL ALWAYS PRINT THE SECOND HIGHEST NUMBER
arr.sort()
maks = (max(arr))
while (max(arr))==maks:
    arr.remove(max(arr))

print (max(arr))
