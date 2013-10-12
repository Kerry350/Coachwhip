from http.server import HTTPServer

class Server():
    def __init__(self, port):
        self.port = port
        self.serverInstance = HTTPServer(('127.0.0.1', port))

    def listen(self):
        self.serverInstance.serve_forever()
        print('"Listening on port {0}: "'.format(self.port))

    def destroy(self):
        self.serverInstance.shutdown()
        self.serverInstance.socket.close()