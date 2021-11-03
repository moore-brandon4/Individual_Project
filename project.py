from flask import Flask, render_template             # import flask framework
app = Flask(__name__)             # create an app instance



@app.route("/")                
def gridbyexample():                    
    return render_template("gridbyexamplerecreate.html") 

@app.route("/zachholman")                
def zachholman():                    
    return render_template("zachholman.html") 

@app.route("/harrypotter")                
def harrypotter():                    
    return render_template("harrypotter.html")           

app.run(debug=True)