from http.server import HTTPServer
from http_.request import requestClassFactory 

"""
 The Server class will be passed a router instance, this router instance
 contains the routeMap that this particular server instance will act
 upon
"""

class Server():
    def __init__(self, port, router):
        self.port = port
        requestHandler = requestClassFactory(router.routeMap)
        print(requestHandler().routeMap)
        self.serverInstance = HTTPServer(('127.0.0.1', port), requestHandler)

    def listen(self):
        print('"Listening on port {0} "'.format(self.port))
        self.serverInstance.serve_forever()
       
    def destroy(self):
        self.serverInstance.shutdown()
        self.serverInstance.socket.close()