#Author: Sai Vusirikapally

#This functions opens a given directory and finds the last modified jommsg*.log files
#Checks the file to determine the data pump status based on the given keywords. 
import sys
from NSCP import log
import glob
import os
def __main__(args):
    start_keyword1 ="DataPump starting in normal state."
    start_keyword2 ="allbacks registered"
    stop_keyword = "closed"
    dir = "DIRECTORY" # Change this directory to actual directory of logs
    #print("{}*.log".format(dir))
    list_of_files = glob.glob("{}*.log".format(dir)) # * means all if need specific format then *.csv

    #print(list_of_files)
    #Get latest file based on it's last modified time
    latest_file = max(list_of_files, key=os.path.getctime) 

    with open(latest_file, 'r') as f:
        content = f.read()
        #search for startword and stopword
        start_pos1 = content.rfind(start_keyword1)
        start_pos2 = content.rfind(start_keyword2)
        if(start_pos1 > start_pos2):
            start_pos = start_pos1
        else:
            start_pos = start_pos2
        stop_pos = content.rfind(stop_keyword)
        #close file handler
        f.close()
    #print("after close")
    #print(start_pos)
    #print(stop_pos)
    #start keyword -- not found && stop key word -- found ---> data pump is off
    if(start_pos == -1 and stop_pos != -1):
        print("Critical: Data pump is off")
        exit(2)  #send data to nagios

    #start keyword -- found && stop key word -- not found ---> data pump is running
    elif (start_pos != -1 and stop_pos == -1): 
        print("OK: Data pump running")
        exit(0)
    elif (start_pos == -1 and stop_pos == -1):
        #start key word -- not found && stop keyword -- not found ---> data pump is running (since there are log records which means data pump is on)
        print("OK: Data pump running")
        exit(0)
    elif (start_pos != -1 and stop_pos != -1):
        #stop key word -- found && start keyword -- found ---> data pump depends
        #if position of start > stopped then data pump is running
        if(start_pos > stop_pos):  
            print("OK: Data pump running")
            exit(0)
        else:
            print("Critical: Data pump is off")
            exit(2)
