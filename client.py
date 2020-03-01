import threading
import time
import random
import socket as mysoc

#client task
def client():
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))


# Define the port on which you want to connect to the server
    port = 50007
    sa_sameas_myaddr =mysoc.gethostbyname(mysoc.gethostname())
# connect to the server on local machine
    server_binding=(sa_sameas_myaddr,port)
    cs.connect(server_binding)
#receive data from the server
    #data_from_server=cs.recv(100)
    #print("[C]: Data received from server::  ",data_from_server.decode('utf-8'))

#open files, read HW1test.txt and add words to List
    f = open("HW1test.txt","r")
    lst = []
    line = f.readline()
    line = line.strip('\n')
    lst.append(line)
    while line:
        line = f.readline()
        line = line.strip('\n')
        lst.append(line)
    #print(lst)
    f.close()
    f = open("HW1out.txt","w")
#send and recieve data
    for i in lst:
        if i == '':
            break
        message = i
        cs.send(message.encode('utf-8'))
        data = cs.recv(256).decode()
        f.write(str(data) + "\n")
        print("from server -> " + str(data))
        #write data to HW1out.txt
        
    f.flush()
    f.close()

# close the cclient socket
    cs.close()
    exit()

t2 = threading.Thread(name='client', target=client)
t2.start()
