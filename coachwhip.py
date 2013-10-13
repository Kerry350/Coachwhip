import json 
from http_.server import Server
from routing.router import Router

class Coachwhip():
    def __init__(self):
        # Config
        configuration = open('config.json')
        data = json.load(configuration)
        configuration.close()
        self.configuration = data

        self.router = Router()
        # self.logger = Logger()

    """
        Once an app instance has been obtained, with app = Coachwhip(), 
        routes can be defined like so:
            
            @app.get('/hello_world')
            def helloWorldHandler():
                print('Handling /hello_world')

        This is achieved using a decorator function
    """
    def get(self, url, **kwargs):
        def decorator(fn):
            self.registerRouteHandler('get', url, fn, kwargs)
            return fn
        return decorator
        
    def post(self, url, **kwargs):
        def decorator(fn):
            self.registerRouteHandler('post', url, fn, kwargs)
            return fn
        return decorator

    def delete(self, url, **kwargs):
        def decorator(fn):
            self.registerRouteHandler('delete', url, fn, kwargs)
            return fn
        return decorator

    def put(self, url, **kwargs):
        def decorator(fn):
            self.registerRouteHandler('put', url, fn, kwargs)
            return fn
        return decorator

    def registerRouteHandler(self, verb, url, fn, kwargs):
        self.router.addRoute(verb, url, fn, kwargs)

    def listen(self, port=None):
        print(self.configuration)
        port = port if port else self.configuration['port']
        self.bootServer(port)

    def bootServer(self, port):
        Server(port, self.router).listen();
