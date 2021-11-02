from flask import Flask, render_template, request          
app = Flask(__name__)                               

@app.route("/")                                 
def home():                                    
    return render_template("index.html")         

@app.route("/page2")                                 
def page2():                    
    return render_template("page2.html")         

@app.route("/contact")                           
def contact():                           
    name = request.args.get('name') if request.args.get('name') else "Hello World!"                            # method called hello
    return render_template("contact.html", aboutName=name)                     

if __name__ == "__main__":                      
    app.run(debug=True)                          