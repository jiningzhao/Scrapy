from socket import *

# 创建socket
tcpSerSocket = socket(AF_INET, SOCK_STREAM)

# 绑定本地信息
address = ('', 8080)
tcpSerSocket.bind(address)

# 	使⽤socket创建的套接字默认的属性是主动的，使⽤listen将其变为被动的，这样就可以接
tcpSerSocket.listen(5)

while True:
    # 如果有新的客户端来链接服务器，那么就产⽣⼀个信⼼的套接字专⻔为这个客户端服务器
    # #	newSocket⽤来为这个客户端服务
    # #	tcpSerSocket就可以省下来专⻔等待其他新客户端的链接
    newSocket, clientSocket = tcpSerSocket.accept()
    while True:
        # 接收对⽅发送过来的数据，最⼤接收1024个字节
        recvData = newSocket.recv(1024)

        if len(recvData) > 0:
            print("192.168.1.105:\n" + recvData.decode('utf8'))
        else:
            break
        # 发送数据到客户端
        sendData = input("127.0.0.1:\n")
        newSocket.send(sendData.encode('utf8'))
    newSocket.close()