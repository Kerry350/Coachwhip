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

        if verb in self.routeMap:
            self.routeMap[verb].append({'url': url, 'handler': fn})
        else:
            self.routeMap[verb] = []
            self.routeMap[verb].append({'url': url, 'handler': fn})

        print(self.routeMap)