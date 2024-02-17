import socket
import sys

if __name__ == "__main__":
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    port = 23202

    if len(sys.argv) > 2:
        port = int(sys.argv[2])

    s.bind(("", port))

    s.listen()

    print(f"Listening on {port}")


    while True:
        client_socket, addr = s.accept()
        print(f"Connection from {addr}")

        req = ""

        while True:
            data = client_socket.recv(4096).decode()
            if not data:
                break
            req += data

            if '\r\n\r\n' in req:
                break

        print("Request: ======================> ", req, sep="\n")

        http_response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nsimple server response"
        client_socket.sendall(http_response.encode('utf-8'))
        client_socket.close()
