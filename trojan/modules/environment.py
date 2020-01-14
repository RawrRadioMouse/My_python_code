import os
#below code retrieves environment variable set on machine,  eg where to install programs, where to put %temp% files and profile settings etc
def run(**args):
        print ("[*] in environment module.")
        return str(os.environ)
