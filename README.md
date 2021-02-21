# Overview

My goal in the development of this application was to gain a basic understanding of the Python socket module, networking, and client-peer connections. 

After starting the server, one may freely connect any number of clients so long as the config file is setup to allow the desired number of connections. Upon starting the client software, one is prompted to input a username by which they will be address, and from thereforward, can send messages to the server to be distributed among other connected clients.

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

I choose to build a client-server model that utilizes a TCP connection to communicate between the server and the connected peers. This allowed for a reliable connection to be estabished and ordered delivery. To establish the connection, port 215 is used. 

By default, Python's .encode() method will utilize UTF-8 encoding.

# Development Environment

- Python 3.8.7 + Socket Module
- Visual Studio Code

# Useful Websites

* [Socket Programming in Python](https://realpython.com/python-sockets/)
* [Python Socket Module Documentation](https://docs.python.org/3/howto/sockets.html)

# Future Work

* Unresolved [Errno 32] Broken Pipe error that has occured randomly after frequent testing.
* Unresolved bug that causes the terminal in Visual Studio Code to dissappear while the code is still running.
* Adding a basic user interface with PySimpleGUI or Tkinter that would facilitate the use of the application.
