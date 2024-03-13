import socket 
import threading
from settings import *

class Network_Handler:
    def __init__(self,game) -> None:
        self.game = game
        self.udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.lobbies = []
        self.players = {}
        self.current_lobby = None
        self.create_lobby_event = False
        self.connected = False

    # TCP SERVER MESSAGES
    def search_for_server(self):
        threading.Thread(target=self.initial_tcp_connect).start()
        
    def initial_tcp_connect(self):
        if self.tcp_server.connect_ex((SERVER_IP,PORT)) == 0:
            self.connected = True
        self.connected = "Failed"

    def recv_tcp(self):
        datatype,data = self.tcp_server.recv(2048).decode("utf-8").split(":")
        
        if datatype == "mapname":
            self.game.map.name = data
        
        elif datatype == "mapdesign":
            mini_map = []
            for row in data.split("/"):
                mini_map.append(row.split(","))
            self.game.map.mini_map = mini_map
        
        elif datatype == "mapsize":
            amount_of_times = data / 2048
            temp = ""
            for time in range(amount_of_times):
                temp += self.server.recv(2048).decode("utf-8")
            rows = temp.split("/")
            mini_map = []
            for row in rows:
                mini_map.append(row.split(","))
            self.game.map.mini_map = mini_map

        elif datatype == "requestmap":
            self.send_map()

        elif datatype == "lobbies":
            if data == "none":
                self.create_lobby_event = True
            else:
                for lobby in data.split("/"):
                    self.lobbies.append(lobby.split(","))

        elif datatype == "lobbyjoin":
            reply,reason = data.split(",")
            if reply == "True":
                self.send_tcp_player_data()
            else:
                print(f"Failed to join server: \n{reason}")

        elif datatype == "playernumber":
            self.game.player.number = int(data)

        elif datatype == "playerinfo":
            name,num,posx,posy,health = data.split(",")
            self.players[name] = {
                "playernum":int(num),
                "posx":float(posx),
                "posy":float(posy),
                "health":int(health)
                }

        elif datatype == "playerleave":
            del self.players[data]

        elif datatype == "gamestarting":
            self.game.started = True

        elif datatype == "gameending":
            self.game.started = False

        else:
            print(f"{datatype}: {data}")

    def request_lobbies(self):
        self.tcp_server.send("lobbiesrequest:PLZ".encode("utf-8"))

    def request_lobby(self,lobby_name):
        if any(lobby_name in lobby for lobby in self.lobbies):
            self.tcp_server.send(f"asktojoin:{lobby_name}".encode("utf-8"))

    def leave_lobby(self):
        self.tcp_server.send(f"leavelobby:{self.current_lobby}".encode())

    def send_tcp_player_data(self):
        msg = f"playerinfo:{self.game.player.name},{self.game.player.pos[0]},{self.game.player.pos[1]},{self.game.player.health}"
        self.tcp_server.send(msg)
    
    def send_map_name(self):
        self.tcp_server.send(f"mapname:{self.game.map.name}".encode("utf-8"))

    def send_map(self):
        self.send_map_name()
        temp = "maplayout:"
        first = True
        for row in self.game.map.custom_map:
            for item in row:
                if first == True:
                    temp = f"{temp}{str(item)}"
                    first = False
                else:
                    temp = f"{temp},{str(item)}"
            temp = f"{temp}/"
        msg = temp.encode("utf-8")
        if len(msg) > 2048:
            self.tcp_server.send(f"mapsize:{str(len(msg))}".encode("utf-8"))
        self.tcp_server.sendall(msg)

    #UDP SERVER MESSAGES
    def sendpos(self,pos):
        msg = f"pos:{pos[0]},{pos[1]}".encode("utf-8")
        self.udp_server.sendto(msg,(SERVER_IP,PORT))