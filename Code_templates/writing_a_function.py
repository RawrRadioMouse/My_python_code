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
unique_comm=["a direct message to your LinkedIn account (you can't even remember setting this up, it still lists your current job as 'Helpdesk monkey. The message appears to be form a throwaway account.'",
             "a twitter DM from someone who lives on a boat called 'Mohn McJaffee...",
             "a letter in the mail with 2 pages of base64...There is no hallmark as to who it could be from other than the insignia of an eagle's head atop a shield",
            ]
rand_entity=["from a contact you made during your 1337 highschool haxx0r days",
             "from your old boss during your time working at an MSP",
             "sent by an anonymous contact",
             "Billy joe bob the triple supreme Ronald Mcdonald of justice",
             "a string of placeholder text",
            ]

choice=('')
def choose_method(choice):
    roll=(int(dice.roll("1d20")))
    
    if roll <= (17):
        choice = random.choice(method_of_comm)
        entity=random.choice(rand_entity)
        print("{} {}".format(choice, entity))
    else:
        choice = random.choice(unique_comm)
        unique_comm.remove(choice)
        print(choice)

    return choose_method

choose_method(choice)

#THIRD EXAMPLE spinning up a listener with threading
def server_loop():
        global target

        
        # if just the listen flag is specified we listen on all
        if not len(target):
                target = "0.0.0.0"
                
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((target,port))
        
        # backlog of 5 incoming requests
        server.listen(5)
        print ("[***] listening on {} {} [***] ".format(target,port))
        
        while True:
                client_socket, addr = server.accept()
                #print ("[\U0001F640] accepted connection from {} {}".format(target,port))
                try:
                # # here we make use of the threading module, we create a new thread for our connecting client AKA your revshell
                        client_thread = threading.Thread(target=client_handler,args=(client_socket,))
                        client_thread.start()
                except Exception as e:
                        print(e)
