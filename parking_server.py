__author__ = 'guille'

from multiprocessing import Process
import utility
import socket               #Import socket module
import Pyro4
import threading

class Server(object):

    def __init__(self,port_server = 1234,host_server = "192.168.1.11",id_parking = 'MON1'):
        self.host_server = host_server
        self.port_server = port_server
        print host_server
        print  self.host_server
        # connect server
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.settimeout(1)
        self.socket_server.connect((host_server, port_server))
        self.socket_server.send("hello from parking")
        #
        self.id_parking = id_parking
        self.local_ip_address = str(utility.ipAdd())
        utility.damon(self,"parking.server")
        # thread = threading.Thread(name='non-block',
        #               target=utility.damon,
        #               args=(self,"parking.server"))
        # thread.start()
        # proc = Process(target=utility.damon, args=(self,"parking.server"))
        # proc.start()
     
    @Pyro4.expose 
    def sendFromArdu(self):
         print "sendFromArdu"
         message = '#' + self.local_ip_address + '#DATE#1'

         self.socket_server.send(message)
         print "sent"
         message_server = self.socket_server.recv(1024)
         print(message_server)
         if (message_server !=''):
             self.add_Vh_Cx(message_server)
    
    @Pyro4.expose
    def sendFromBar(self,message):
        print "sendFromBar"
        message = '#'+ self.local_ip_address + '#PARKING#' + message
        print message
        self.socket_server.send(message)
        print "sent"
        message_server = self.socket_server.recv(1024)
        print(message_server)
        if (message_server != ''):
            message_server = message_server.split('#')
            print(message_server)
            if (message_server[2]=='PARKING') and (message_server[3]=='1'):
                serial_com = Pyro4.Proxy("PYRONAME:serial_com.client")
                serial_com.sendMsgToArdu("#BARR#0000000000000000001#\n")
    
    @Pyro4.expose
    def add_Vh_Cx(self,message):
        message = message.split("#")
        message[3] = message[3].replace("-", "")
        msg_printer = message[3] + self.id_parking
        print(msg_printer)
        message = '#' + self.local_ip_address + '#PRINTER#' + msg_printer
        self.socket_server.send(message)
        message_server = self.socket_server.recv(1024)
        message_server = message_server.split("#")
        print(message_server)
        if (message_server[2] == 'PRINTER') and (message_server[3] == '1'):
             serial_com = Pyro4.Proxy("PYRONAME:serial_com.client")
             serial_com.sendDataToArdu("#BARR#0000000000000000001#\n")

server = Server(4321,utility.ipAdd())