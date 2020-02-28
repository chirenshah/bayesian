import pandas
import math

def bay(rown,cond):
	if(rown == "age"):	
		condition = {1:"<=30",2:"31-40",3:">40"}
	if(rown == "income"):
		condition = {1:"high",2:"medium",3:"low"}
	if(rown == "student"):
		condition = {1:"yes",2:"no"}
	if(rown == "credit_rating"):
		condition = {1:"excellent",2:"fair"}
	y = 0.0
	n = 0.0
	ryes = 0.0
	rno = 0.0
	count =0.0
	category = condition[cond]
	df = pandas.read_csv("info.csv")
	row = df["buys_comp"]
	#print(row)
	for row in row:
		if row == "yes":
			y = y +1 
		else:
			n = n + 1
	pyes = y/14.0
	pno = n/14.0
	print(n,pno)
	pname = df[rown]
	for i,j in df.iterrows():
		#print(i,j["age"])
		if j[rown] == category:
			if j["buys_comp"] == "yes":
				ryes = ryes + 1
			else:
				rno = rno + 1 
	if ryes == 0.0:
		ryes = ryes + 1
		proby = ryes/y+1
	else:
		proby = ryes/y
	if rno == 0.0 :
		rno = rno + 1
		probn = rno/n+1
	else:
		probn = rno/n
	return [ryes,rno,proby,probn,pyes,pno]

def calc():
	age = bay("age",1)
	income = bay("income",2)
	student = bay("student",2)
	credit_rating = bay("credit_rating",1)
	probyes = age[4]*age[2]*income[2]*student[2]*credit_rating[2]
	probno = age[5]*age[3]*income[3]*student[3]*credit_rating[3]
	print( probyes,probno)

calc()
