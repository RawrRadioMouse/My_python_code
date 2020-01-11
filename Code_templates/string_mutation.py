#Input Format
#The first line contains a string, s.
#The next line contains an integer i, denoting the index location and a character c separated by a space.
#
#Output Format
#Using any of the methods explained above, replace the character at index i with character c.


def mutate_string(string, position, character):
    l=list(s)
    j=(int(i))
    l[j]=c
    joiner=''
    return (joiner.join(l))

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
