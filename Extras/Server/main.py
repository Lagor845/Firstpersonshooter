import socket
from threading import Thread

"""
General layout for storing user data
ServerManager => lobbies = {
    "Lobbyname" : [List of people joined]
}
ServerManager => clients = {
    "Ip address" : {
        "lobby" : "Lobbyname",
        "connection" : conn,
        "name" : "name",
        "x pos" : x,
        "y pos" : y,
        "health" : health
    }
}
"""

class Tcp_Server:
    def __init__(self) -> None:
        pass

    def start(self,server_manager):
        self.server_manager = server_manager
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((socket.gethostbyname(socket.gethostname()),61000))
        print("TCP SERVER CREATED SUCCESSFULLY")
        self.server.listen()
        self.accept()

    def accept(self):
        while True:
            conn,addr = self.server.accept()
            self.server_manager.clients[addr[0]] = {"connection":conn,"inlobby":False,}
            print(f"[{addr[0]}] has connected...")
            Thread(target=self.recv,args=(addr[0],)).start()

    def recv(self,address):
        connected = True
        while connected:
            try:
                datatype,data = self.server.recv(2048).decode("utf-8").split(":")
            except:
                print(f"[{address}] has disconnected...")
                connected = False
            
            if connected != False:
                if datatype == "lobbiesrequest":
                    print(f"[{address}] has requested lobbies...")
                    lobbies = list(self.server_manager.lobbies.keys())
                    temp = "lobbies:"
                    if len(lobbies) != 0:
                        first = True
                        for lobby in lobbies:
                            if first == True:
                                temp = f"{temp}{lobby},{len(self.server_manager.lobbies[lobby])}"
                                first = False
                            else:
                                temp = f"{temp}/{lobby},{len(self.server_manager.lobbies[lobby])}"
                        self.server_manager.clients[address]["connection"].send(temp.encode("utf-8"))
                    else:
                        temp = temp + "none"
                        self.server_manager.clients[address]["connection"].send(temp.encode("utf-8"))

                elif datatype == "asktojoin":
                    print(f"[{address}] has joined {data}...")
                    self.server_manager.lobbies[self.server_manager.clients[address]["lobby"]].remove(address)
                    if len(self.server_manager.lobbies[self.server_manager.clients[address]["lobby"]]) == 0:
                        del self.server_manager.lobbies[self.server_manager.clients[address]["lobby"]]
                    self.server_manager.lobbies[data].append(address)
                    self.server_manager.clients[address]["lobby"] = data
                    msg = f"playerinfo:{self.server_manager.clients[address]["name"]},{len(self.server_manager.lobbies[data]) + 1},{self.server_manager.clients[address]["xpos"]},{self.server_manager.clients[address]["ypos"]},{self.server_manager.clients[address]["health"]}"
                    times = 1
                    for ip in self.server_manager.lobbies[data]:
                        self.server_manager.clients[ip]["connection"].send(msg.encode("utf-8"))
                        if ip != address:
                            send_to_client = f"playerinfo:{self.server_manager.clients[ip]["name"]},{times},{self.server_manager.clients[ip]["xpos"]},{self.server_manager.clients[ip]["ypos"]},{self.server_manager.clients[ip]["health"]}"
                            self.server_manager.clients[address]["connection"].send(send_to_client.encode("utf-8"))
                            times += 1

                elif datatype == "leavelobby":
                    print(f"[{address}] has left {data}...")
                    self.server_manager.lobbies[self.server_manager.clients[address]["lobby"]].remove(address)
                    for ip_address in self.server_manager.lobbies[self.server_manager.clients[address]["lobby"]]:
                        self.server_manager.clients[ip_address]["connection"].send(f"playerleave:{self.server_manager.clients[address]["name"]}".encode("utf-8"))

                elif datatype == "mapname":
                    self.server_manager.lobbies[self.server_manager.clients[address]["lobby"]]["mapname"] = data

                elif datatype == "maplayout":
                    print(f"[{address}] has sent map...")
                    self.server_manager.lobbies[self.server_manager.clients[address]["lobby"]]["maplayout"] = data

                elif datatype == "mapsize":
                    amount_of_times = data / 2048
                    temp = ""
                    for time in range(amount_of_times):
                        temp += self.server.recv(2048).decode("utf-8")
                    self.server_manager.lobbies[self.server_manager.clients[address]["lobby"]]["maplayout"] = temp

                elif datatype == "playerinfo":
                    print(f"[{address}] has sent in player data...")
                    name,x,y,health = data.split(",")
                    try:
                        self.server_manager.lobbies[name]
                        self.server_manager.clients[address]["connection"].send("name_success:Name already taken".encode("utf-8"))
                    except:
                        self.server_manager.lobbies[name] = [address]
                        self.server_manager.clients[address]["lobby"] = name
                        self.server_manager.clients[address]["connection"].send("name_success:SUCCESS".encode("utf-8"))
                        self.server_manager.clients[address]["name"] = name
                        self.server_manager.clients[address]["xpos"] = x
                        self.server_manager.clients[address]["ypos"] = y
                        self.server_manager.clients[address]["health"] = health
                        print(f"New lobby created under the name of {name}")

        self.server_manager.lobbies[self.server_manager.clients[address]["lobby"]].remove(address)
        for ip_address in self.server_manager.lobbies[self.server_manager.clients[address]["lobby"]]:
            self.server_manager.clients[ip_address]["connection"].send(f"playerleave:{self.server_manager.clients[address]["name"]}".encode("utf-8"))
        del self.server_manager.clients[address]

class Udp_Server:
    def __init__(self) -> None:
        pass

    def start(self,server_manager):
        self.server_manager = server_manager
        self.server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.server.bind((socket.gethostbyname(socket.gethostname()),61000))
        print("UDP SERVER CREATED SUCCESSFULLY")
        while True:
            msg,addr = self.server.recv(2048)

class Server_Manager:
    def __init__(self) -> None:
        self.clients = {}
        self.lobbies = {}
        self.udp_server = Udp_Server()
        Thread(target=self.udp_server.start,args=(self,)).start()
        self.tcp_server = Tcp_Server()
        self.tcp_server.start(self)

def main():
    Server_Manager()

main()