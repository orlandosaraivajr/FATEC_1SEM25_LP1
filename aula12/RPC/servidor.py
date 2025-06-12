# Servidor XML-RPC
from xmlrpc.server import SimpleXMLRPCServer

def soma(x, y):
    return x + y

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(soma, "soma")
server.serve_forever()
