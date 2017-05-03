__author__ = 'guille'
import socket
import utility
import time



#Local Server
socket_localhost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #Create a new object socket
host_server_localhost = str(utility.ipAdd())                           #Localhost server ip address
print(host_server_localhost)
localhost_port = 4321                                                 #Localhost server port
socket_localhost.bind((host_server_localhost,localhost_port))           #Localhost server binding port
socket_localhost.listen(5)
conn, addr = socket_localhost.accept()


def Principal():

    while True:
        try:

            message = conn.recv(1024)
            if message != '':
                print(message)
                message_client = message.split("#")
                print(message_client[2])
                print(message_client)
                if message_client[2] == 'DATE':
                    conn.send( '#foo#bar#DATE#-message-')
                elif message_client[2] == 'PRINTER':
                    print 'PRINTER'
                    conn.send( '#foo'+message)
                elif message_client[2] == 'PARKING':
                    print('PARKING')
                    conn.send('#foo#bar#PARKING#1#')
        except:
            pass



Principal()

