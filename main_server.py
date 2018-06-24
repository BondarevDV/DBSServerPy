# Модуль socketserver для сетевого программирования
from socketserver import *
from CUDPServer import UDPServer
# данные сервера
host = 'localhost'
port = 777



if __name__ == "__main__":
    # Создаем экземпляр класса
    UDPServer server(host,port)
    #server = UDPServer(addr, MyUDPHandler)
    #print('starting server... for exit press Ctrl+C')
    # serve_forever - запускаем сервер
    #server.serve_forever()
