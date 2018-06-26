import socket
import datetime
import sys

class UDPServer:
    udp_socket = None
    OnWork = False
    size_file_reg = 50000
    size = 1024
    conn = None
    addr = None
    host = "0.0.0.0"
    port = 8001
    buffer = []
    current_time = ""
    file = None
    def __init__(self,host, port):
        self.host = host
        self.port = port
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind((self.host,self.port))

    def createRegFile(self):
        self.file = open(datetime.now, "wb")

    def SetSizeBuffer(self, size_buff):
        self.size = size_buff

    def SetNetSettings(self, host, port):
        self.host = host
        self.port = port

    def Send(self):
        self.udp_socket.sendto(self.buffer, (self.host, self.port))


    def ProccesingDGRAM(self,buffer):

        current_size = self.file.tell()
        #print(current_size)
        for byte in range(len(buffer)):
            if current_size < self.size_file_reg:
                self.file.write(byte)
            else:
                self.file.close()
                self.createRegFile()

    def Stop(self):
        OnWork = False
        self.file.close()

    def Start(self):
        self.current_time = datetime.now
        self.createRegFile()
        OnWork = True
        while self.OnWork:
            buffer, addr = self.udp_socket.recvfrom(self.size)
            print("received message:", buffer)
