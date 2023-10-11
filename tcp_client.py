import socket, sys, threading

def tcp_client():
    c_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_s.connect(("127.0.0.1", 8888))
    while True:
        msg = input("$ ")
        c_s.send(msg.encode())

def main():
    thread = threading.Thread(target=tcp_client)
    thread.start()


main() if __name__ == "__main__" else sys.exit(1)