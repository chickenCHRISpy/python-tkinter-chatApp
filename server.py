import socket
import threading

# print(socket.gethostbyname(socket.gethostname()))
#connection
PORT=3000
HOST=socket.gethostbyname(socket.gethostname())
ADDRESS=(HOST,PORT)
FORMAT= "utf-8"

clients=[]
names=[]

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDRESS)

#starting the chat
def startChat():
    print(f"Server is working on {HOST}")

    server.listen()

    while True:
        connection, addr = server.accept()
        connection.send("NAME".encode(FORMAT))

        name = connection.recv(1025).decode(FORMAT)

        names.append(name)

        clients.append(connetion)

        print(f"Name is: {name}")

        broadcastMessage(f"{name} has joined the chat".encode(FORMAT))

        connection.send("Connection successful!".encode(FORMAT))

        thread = threading.Thread(target=receive,args=(connection,addr))

        thread.start()

        print(f"Active connections {threading.active_count()-1}")

#recieving the message

def receive(connection, addr):
    print("New Connection{addr")
    
    connected = True
    
    while connected:
        message = connection.recv(1025)

        broadcastMessage(message)

    connection.close()

#broadcasting message
def broadcastMessage(message):
    for client in clients:
        client.send(message)

startChat()
    
    