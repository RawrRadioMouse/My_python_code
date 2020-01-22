#FIRST EXAMPLE - PRINT OUTSIDE FUNCTION:

def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                is_leap=True
            else:
                is_leap=False
        else:
            is_leap=True
    
    else:
        is_leap=False
    return is_leap

year = int(input())
print(is_leap(year))


#SECOND EXAMPLE - PRINT INSIDE FUNCTION:

import random
import dice

method_of_comm=["an sms on your burner sim",
                "a Discord invite to a private chat",
                "an email to your protonmail address",
                "a twitter mention directing you to an onion link to an IRC",
                ]
unique_comm=["a direct message to your LinkedIn account (you can't even remember setting this up, it still lists your current job as 'Helpdesk monkey'",
             "a twitter DM from someone who lives on a boat called 'Mohn McJaffee...",
             "a letter in the mail with 2 pages of base64.......",
            ]

choice=('')
def choose_method(choice):
    roll=(int(dice.roll("1d20")))    
    if roll <= (17):
        choice = random.choice(method_of_comm)
        print(choice)
    else:
        choice = random.choice(unique_comm)
        unique_comm.remove(choice)
        print(choice)
        print(unique_comm)
    return choose_method

choose_method(choice)
