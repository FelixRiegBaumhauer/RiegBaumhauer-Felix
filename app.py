from flask import Flask
app=Flask(__name__)

@app.route("/")
def helloworld():
    return "hello world"

@app.route("/StepOne")
def step1():
    return "you completted step 1"

@app.route("/StepTwo")
def step2():
    return "you completed step 2"

@app.route("/StepThree")
def step3():
    return "step three completed, \n 100% completion, \n... \n... \n    Noah"

def foo():
    print "Noah"
if __name__=="__main__":
    app.run()
    
