"""
    This is the actual test app file, which uses the Coachwhip MVC to 'do something'
"""

from coachwhip import Coachwhip

app = Coachwhip()

@app.get('/hello_world')
def helloWorldHandler():
    print("Hello World!")

app.listen(7000)