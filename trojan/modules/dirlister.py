import os
#run takes a variable number of args
def run(**args):
        
        print ("[]* in dirlister module.")
        #lists files in current directory and then prints as a string with "." after each folder
        files = os.listdir(".")
        return str(files)
