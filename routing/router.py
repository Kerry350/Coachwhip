import pprint

# Takes the default environ dictionary and formats it in a slightly nicer way
def parseEnviron(environ):
    data = {}
    
    data['url'] = environ['PATH_INFO']
    data['content_length'] = environ['CONTENT_LENGTH']
    data['accepts'] = environ['HTTP_ACCEPT']
    data['user_agent'] = environ['HTTP_USER_AGENT']
    data['protocol'] = environ['SERVER_PROTOCOL']
    data['connection'] = environ['HTTP_CONNECTION']
    data['host'] = environ['HTTP_HOST']
    data['cookies'] = environ['HTTP_COOKIE']
    data['port'] = environ['SERVER_PORT']
    data['method'] = environ['REQUEST_METHOD']
    data['query_string'] = environ['QUERY_STRING']
    data['content_type'] = environ['CONTENT_TYPE']

    return data

class Router():
    def __init__(self):
        """
            routeMap is a dictionary of all the verb and url combinations, and the 
            handler that should be called if a match happens
        """
        self.routeMap = {}
    
    def addRoute(self, verb, url, fn, kwargs):
        print(verb)
        print(url)
        print(fn)
        print(kwargs)

        if verb not in self.routeMap:
            self.routeMap[verb] = []
        
        self.routeMap[verb].append({'url': url, 'handler': fn})
            
        print(self.routeMap)

    def handleRequest(self, environ, start_response):

        pprint.pprint(parseEnviron(environ))

        output = "Hello World".encode('UTF-8')
        status = '200 OK'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)

        return [output]