import threading
import time
import random
import socket as mysoc

# server task
def server():
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    server_binding=('',50007)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)
    csockid,addr=ss.accept()
    print ("[S]: Got a connection request from a client at", addr)
# send a intro  message to the client.
    #msg="Welcome to CS 352"
    #csockid.send(msg.encode('utf-8'))

#send and recieve data
    
    data = csockid.recv(100).decode()

    while data != '':
        print("from client -> " + str(data))
        message = ""
        if not data:
            print("BREAK")
            break
        for i in data:
            message += str(ord(i)) + "_"    
        csockid.send(message.encode("utf-8"))
        data = csockid.recv(100).decode()

   # Close the server socket
    ss.close()
    exit()

t1 = threading.Thread(name='server', target=server)
t1.start()