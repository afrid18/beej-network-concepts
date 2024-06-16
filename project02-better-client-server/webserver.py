import socket
import sys
import os
import magic

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

            if "\r\n\r\n" in req:
                break

        print("Request: ======================> ", req, sep="\n")

        reqs_list = req.split("\r\n")
        file = reqs_list[0].split(" ")[1].split("/")[-1]

        print("User is requesting", file)
        file_ext = os.path.splitext(file)[1]

        # set content type
        content_type = ""
        # if file_ext == "html":
        #     content_type = "text/html"
        # else:
        #     content_type = "text/plain"

        # Send the response with the file if the file is present,
        # else send 404 with file not found

        try:
            with open(file, "rb") as f:
                content_type = magic.from_file(file, mime=True)
                buf = f.read()
                http_response = (
                    f"HTTP/1.1 200 OK\r\nContent-Type: \
                {content_type}\r\nContent-Length: \
                {len(buf)}\r\n\r\n".encode("utf-8") + buf)
                client_socket.sendall(http_response)
                client_socket.close()

        except FileNotFoundError:
            http_response = f"HTTP/1.1 404 Not Found\r\nContent-Type: \
            {content_type}\r\nContent-Length: 0\r\n\r\nFile Not Found"
            client_socket.sendall(http_response.encode("utf-8"))
            client_socket.close()
