import os               
from flask import Flask, render_template     #import flask object from flask module

app = Flask(__name__)

@app.route('/')    #route decorator binds index function to itself so when root is called...function is called 
def index():    #returns a template from index function
    return render_template("index.html")
    

@app.route('/about')        #route is also called a view . whever we navigate to /about..it will return about template       
def about():
    return render_template("about.html", page_title="About", list_of_numbers=[1, 2, 3])
    
    
@app.route('/contact')              #decorator @app.route. path is "contact". bind to a view(route) called contact() 
def contact():
    return render_template("contact.html", page_title="Contact")
    

@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")
    
    
if __name__ == '__main__':       
    app.run(host=os.environ.get('IP'),          
            port=int(os.environ.get('PORT')),
            debug=True)    
            
            
            
#tell flask what IP address we want to run this on
#port we want to open. cast that to an int
#pass in the host name.#.environ.get allows us get IP address.
#be able to do debugging 