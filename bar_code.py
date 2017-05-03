__author__ = 'guille'

import Pyro4
from multiprocessing import Process
import sys


class BarCode(Process):
    def __init__(self):
        # proc = Process(target=self.run, args=())
        # proc.start()
        super(BarCode, self).__init__()

    def run(self):
        while True:
            try:
                # line = sys.stdin.readline().rstrip()
                line = "123456"
                if line != '':
                    print ('Codigo de barras ' + line)
                    parking_server = Pyro4.Proxy("PYRONAME:parking.server")
                    parking_server.sendFromBar('123456')
            except:
                continue


barcode = BarCode()
barcode.start()
