import socket, threading, sys


def udp_client():
    c_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = input("$ ")
        c_s.sendto(message.encode(), ("127.0.0.1", 8890))


def main():
    thread = threading.Thread(target=udp_client)
    thread.start()

main() if __name__ == "__main__" else sys.exit(1)