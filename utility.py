__author__ = 'guille'

import commands		        #Import library to execute linux terminal commands
import Pyro4

def ipAdd():
    intf = 'eth0'
    intf_ip = commands.getoutput("ip address show dev " + intf).split()
    intf_ip = intf_ip[intf_ip.index('inet') + 1].split('/')[0]
    return intf_ip

#Crea un demonio o sea un servicio con el nombre q le des que despues puede ser usado para establecer comunicion de otros
#procesos con est
def damon(self,name):
    daemon = Pyro4.Daemon()  # make a Pyro daemon
    ns = Pyro4.locateNS()  # find the name server
    uri = daemon.register(self)  # register the save maker as a Pyro object
    ns.register(name, uri)  # register the object with a name in the name server
    print("Server "+name+ " Ready.")
    daemon.requestLoop()  # start the event loop of the server to wait for calls


