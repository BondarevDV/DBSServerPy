import socket

# обработчик запросов UDP подкласс DatagramRequestHandler
# Этот класс работает аналогично классу TCP, за исключением того,
# self.request состоит из пары данных и сокета клиента,
# так как нет никакой связи адрес, клиент должен быть явно указан при отправке данных обратно через SendTo()
class UDPServer:
    self.OnWork
    self.conn
    self.addr
    def __init__(self,host, port):
        udp_socket = socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind(host,port)
        udp_socket.listen(socket.SOMAXCONN)
        conn, addr = udp_socket.accept()

    def Start(self):
        while self.OnWork:
            data = self.conn