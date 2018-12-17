import os
import json
from flask import Flask, render_template     #import flask object from flask module

app = Flask(__name__)

@app.route('/')    #route decorator binds index function to itself so when root is called...function is called 
def index():    #returns a template from index function
    return render_template("index.html")
    

@app.route('/about')        #route is also called a view . whever we navigate to /about..it will return about template       
def about():
    data = []               #empty array called data
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)                     #set data variable to json parsed data we sent through
    return render_template("about.html", page_title="About", company = data) #list_of_numbers=[1, 2, 3]
                                    #pass into return company = data. in template refer to data passed through as company
         
@app.route("/about/<member_name>")          
def about_member(member_name):      #new view..about_member with argument member_name
    member = {}                     #empty object to store data in
    
    with open("data/company.json", "r") as json_data: #open comp.json for reading and refer to as json_data
        data = json.load(json_data)     #create another var inside where we pass the data that we've passed through and convert into json
        for obj in data:                    #iterate through data array
            if obj["url"] == member_name:   #if url in that element of our array = member name
                member = obj             #member obj = current object
                
    return render_template("member.html", member=member)
    
    
    
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