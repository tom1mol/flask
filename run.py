import os               
from flask import Flask, render_template     #import flask object from flask module

app = Flask(__name__)

@app.route('/')     #forward slash as a string
def index():
    return render_template("index.html")
    

@app.route('/about')
def about():
    return render_template("about.html")
    
    
@app.route('/contact')
def contact():
    return render_template("contact.html")
    
    
if __name__ == '__main__':       
    app.run(host=os.environ.get('IP'),          
            port=int(os.environ.get('PORT')),
            debug=True)    
            
            
            
#tell flask what IP address we want to run this on
#port we want to open. cast that to an int
#pass in the host name.#.environ.get allows us get IP address.
#be able to do debugging 