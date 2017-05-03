__author__ = 'guille'
import serial               #Import serial module
from multiprocessing import Process
import Pyro4
import utility

class SerialCom(Process):
    def __init__(self):
        #self.serial = serial.Serial('/dev/ttyAMA0', 9600)
        super(SerialCom, self).__init__()
        proc = Process(target=utility.damon, args=(self,"serial_com.client"))
        proc.start()

    def run(self):
         while True:
             #rcv = self.serial.read(27)
             rcv = '#BOTO#00000000000000000001#'
             print(rcv)
             if(rcv == '#BOTO#00000000000000000001#'):
                 parking_server = Pyro4.Proxy("PYRONAME:parking.server")
                 parking_server.sendFromArdu()

    def sendMsgToArdu(self,data):
        print(data)
         #self.serial.write(data)

serial = SerialCom()
serial.start()