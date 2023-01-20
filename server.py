from lib.networking import *
import threading

server = connection()
server.bind()
print(f"{server.adress[0]}:{server.adress[1]}")


clients = []



# Flags
#
# "leave" : tells server client left
# "msg" : tells client to print out message
# "nick" : contains the clients nickname
#



def brodcast(msg,flag):
    print(msg)
    for client in clients :  
        client.send(msg,flag)
    pass


def client_handle(conn:connection):
    #recive mmesages from clients then brodcast them to all other clients
    client_nick = "N/A"
    while True:
        msg , flag = conn.recv()
        if flag == "leave" :
            break
            pass
        elif flag == "nick":
            client_nick = msg
            print(f"conn : {conn} , nickname : {client_nick}")
            brodcast(f"<server> {client_nick} joined","msg")
        elif flag == "msg":
            msg = f"[{client_nick}] : {msg}"
            brodcast(msg,flag)
    # on client leave , remove client form list of clients :

    clients.pop(clients.index(conn))
    print(f"client '{client_nick}' discconected")
    brodcast(f"<server> {client_nick} left","msg")
    conn.close()
    pass



# wait for clients to connect then start a thread for them
while True :
    print("awaiting new connection")
    client_conn , client_addr = server.listen()
    print(f"connected by {client_addr}")
    clients.append(client_conn)
    threading.Thread(target=client_handle,args=(client_conn,)).start()
    pass


