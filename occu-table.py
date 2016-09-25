from flask import Flask, render_template
import random

app=Flask(__name__)

@app.route("/") #recyclyed, 
def helloworld():
    return "To access, type occupations in the top thing"


@app.route("/StepOne")
def step1():
    return "you completted step 1"

@app.route("/StepTwo")
def step2():
    return "you completed step 2"

@app.route("/StepThree")
def step3():
    return "step three completed, \n 100% completion, \n... \n... \n    Noah"

#@app.route("/FirstTemp")
#def test_temp():
#    return render_template("temp.html", foo ="This is the best title", fool=di#ct)should return a render template

#---------------------------------------------------------#
#The other code


# Opens and reads file into stringthing
file=open("occupations.csv", "r")
stringthing = file.read()

# Splits the string into an array called splitString
splitString = str.split(stringthing, "\r\n")

dict = {}

# Loops through array line by line
for line in splitString:
	if "Total" not in line:
		if len(line)>0 and line[0]=='"':
			line = line[1:]
			dict[float(line[line.index('"')+2:])]=line[0:line.index('"')]
		elif len(line)>0 and splitString.index(line)!=0:
			#print line
			dict[float(line[line.index(',')+1:])]=line[0:line.index(',')]
        
#print dict

#because we have to make this a function...
def getRandomOccupation():
	#get a random number from 0 to 997 <-- although the toal is 99.8, we're working with integers and randint() is inclusive of zero
	r = random.randint(0,997)
	temp = 0 #keeps track of probability range
	for key in dict:
		temp += 10 * key
		if r < temp:
			return dict[key]
		if temp == 859:
			return dict[key]
    
        
#print getRandomOccupation()
#print quickText()

#jobs = []
#nums = []
#for key in dict:
#    nums.append(key)
#    jobs.append(dict[key])

file.close()


@app.route("/occupations")
def occupater():
    return render_template("occu-temp.html",coll=dict, name="A Collection of Occupations", ans = getRandomOccupation())#should return a render template

    
if __name__=="__main__":
    app.run()
    app.debug = True #this is comment
    

