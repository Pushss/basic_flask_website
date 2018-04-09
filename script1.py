from flask import Flask

app=Flask(__name__) #instantiate objec/create instance(will get name of python script)

@app.route('/')#Decorator(sets home)
def home():
    return "Website homepage!" #returns text

@app.route('/about/')#Decorator(sets about)
def about():
    return "This is the about page!" #returns text

if __name__ == "__main__": #if script1.py equals __main__ then run.
    app.run(debug=True)#runs app
