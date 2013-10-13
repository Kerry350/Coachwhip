from http.server import BaseHTTPRequestHandler

def requestClassFactory(routeMap):
    class RequestHandler(BaseHTTPRequestHandler):
        def __init__(self):
            self.routeMap = routeMap
            
    return RequestHandler