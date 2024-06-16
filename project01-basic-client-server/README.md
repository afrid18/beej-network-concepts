This is a basic client-server project, written in python, following [beej's guide](https://beej.us/guide/bgnet0/).

# Get Started

## Server

The default port on which the server runs is `port = 23202`.

Run `python webserver.py` optionally you can also give a custom port as
`python webserver.py 23789`


## Client

The client request the server(HTTP) on the default port of 80(for HTTP)

Run `python clientserver.py www.google.com` this command will give the output
that has headers information and the html of the particular site, in this case
google's
