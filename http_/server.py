from wsgiref.simple_server import make_server
from http_.request import requestClassFactory 

"""
 The Server class will be passed a router instance, this router instance
 contains the routeMap that this particular server instance will act
 upon
"""

class Server():
    def __init__(self, port, router):
        self.port = port
        self.serverInstance = make_server('127.0.0.1', port, router.handleRequest)

    def listen(self):
        print('"Listening on port {0} "'.format(self.port))
        self.serverInstance.serve_forever()
       
    def destroy(self):
        self.serverInstance.shutdown()
        self.serverInstance.socket.close()