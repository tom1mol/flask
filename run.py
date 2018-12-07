import os               
from flask import Flask     #import flask object from flask module

app = Flask(__name__)

@app.route('/')     #forward slash as a string
def hello():
    return "Hello World"  #output hello world to browser
    
    
if __name__ == '__main__':       
    app.run(host=os.environ.get('IP'),          
            port=int(os.environ.get('PORT')),
            debug=True)    
            
            
            
#tell flask what IP address we want to run this on
#port we want to open. cast that to an int
#pass in the host name.#.environ.get allows us get IP address.
#be able to do debugging 