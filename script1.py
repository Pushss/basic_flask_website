from flask import Flask, render_template

app=Flask(__name__) #instantiate object/create instance(will get name of python script)
app.debug=True

@app.route('/')#Decorator(sets home)
def home():
    return render_template("home.html") #returns text

@app.route('/about/')#Decorator(sets about)
def about():
    return render_template("about.html") #returns text

if __name__ == "__main__": #if script1.py equals __main__ then run.
    app.run(debug=True)#runs app
