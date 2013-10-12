"""  app = Coachwhip() 
"""

import json 
from http_.server import Server

class Coachwhip():
    def __init__(self):
        # Config
        configuration = open('config.json')
        data = json.load(configuration)
        configuration.close()
        self.configuration = data

        # self.router = Router()
        # self.logger = Logger()

    def get(self):
        self.registerRouteHandler(args)

    def  post(self):
        self.registerRouteHandler(args)

    def delete(self):
        self.registerRouteHandler(args)

    def put(self):
        self.registerRouteHandler(args)

    def registerRouteHandler(self):
        print('Registering route handler')

    def listen(self, port=None):
        port = port if port else self.configuration.port
        self.bootServer(port)

    def bootServer(self, port):
        Server(port).listen();
