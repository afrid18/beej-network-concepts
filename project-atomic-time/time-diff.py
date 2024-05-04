import socket
import time


def system_seconds_since_1900():
    """
    return the number of seconds since 1900
    """

    seconds_delta = 2208988800
    seconds_since_unix_epoch = time.time()
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return int(seconds_since_1900_epoch)


def main():
    server = 'time.nist.gov'
    port = 37

    # create a socket
    s = socket.socket()

    # connect to the server
    s.connect((server, port))

    # receive the response
    response = s.recv(4)

    # close the connection
    s.close()

    # convert the response to an integer
    seconds = int.from_bytes(response, 'big')

    print('NIST Time: {}'.format(seconds))
    print('System Time: {}'.format(system_seconds_since_1900()))


if __name__ == '__main__':
    main()
