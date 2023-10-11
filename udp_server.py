import socket, threading, sys

def udp_server():
    s_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s_s.bind(("0.0.0.0", 8890))
    print("Listening on 8890:")
    while True:
        data, addr = s_s.recvfrom(1024)
        print("Received from {}: {}".format(addr, data.decode()))

def main():
    thread = threading.Thread(target=udp_server)
    thread.start()


main() if __name__ == "__main__" else sys.exit(1)