import socket
import sys


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python script.py <URL> [<Port>]")
    else:
        s = socket.socket()
        url = str(sys.argv[1])
        port = 80
        if len(sys.argv) > 2:
            port = int(sys.argv[2])
        s.connect((sys.argv[1], port))

        # build request
        request = f"GET / HTTP/1.1\r\nHost: {url}\r\nConnection: close\r\n\r\n"

        # send a request
        s.sendall(request.encode())

        # receive a response
        res = b""

        while True:
            data = s.recv(4096)
            if not data:
                break
            res += data

        s.close()


        response_decoded = res.decode('utf-8', 'ignore')

        headers, _, body = response_decoded.partition('\r\n\r\n')

        print(headers, body, sep="\n")

