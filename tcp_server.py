import socket, sys, threading

def tcp_server():
    s_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_s.bind(("0.0.0.0", 8888))
    s_s.listen(5)
    print("Listening on 8888:")
    while True:
        c_s, _ = s_s.accept()
        thread = threading.Thread(target=handle_client, args=(c_s,))
        thread.start()

def handle_client(c_s):
    while True:
        data = c_s.recv(1024)
        if data:
            print("Received:", data.decode())
        else:
            break

def main():
    thread = threading.Thread(target=tcp_server)
    thread.start()

main()  if __name__ == "__main__" else sys.exit(1)
