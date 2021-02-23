"""
Calorie Calculator 

Author: Sean-Michael Woerner
Date: 02/04/2021

"""




def print_menu():
	print("*******************************************")
	print("*	  Calorie Calculator              *")
	print("*                                         *")
	print("*        by: Sean-Michael Woerner         *")
	print("*******************************************")
	print("\nMain Menu\n---------")
	print("(1) Calculate BMR")
	print("(2) Calculate Calories Needed to Lose Weight")
	print("(3) Calculate Calroies Needed to Gain Weight")
	print("---------------------------------------------")
	
#This method uses the Harris-Benedict Formula	

def getBMR(gender, age, height, weight, act_level):
	#Male
	if(gender==1):
		bmr = 66.47 + (6.24*weight) + (12.7*height) - (6.755*age)	
	#Female	
	if(gender==2):
		bmr = 655.1 + (4.35*weight) + (4.7*height) - (4.7*age)

	return (float(bmr*act_level))
	

def personData():
	gender = int(input("What is your gender?\n(1) Male\n(2) Female\n"))
	"""
	if((gender != 1) or (gender !=2)):
		print("Error, exiting...")
		exit()
	"""
	age = int(input("What is your age?\n"))
	height = float(input("What is your height in inches?\n"))
	weight = float(input("What is your weight in pounds?\n"))
	act_level = float(input("What is your activity level?\n(1.2) Sedentary\n(1.375) 1-3 days of exercise per week\n(1.55) 3-5 days of exercise per week\n(1.725) 6-7 days of exercise per week\n(1.9) Very hard exercise daily\n(x) Or enter a custom activity level\n"))
	
	
	return gender,age,height,weight,act_level

def printBMR():
	gender,age,height,weight,act_level = personData()
	bmr = getBMR(gender,age,height,weight,act_level)
	
	print("\nYour Calculated BMR is: "+str(bmr)+" calories burned per day.")
	back = input("Press ENTER to return...\n")

def loseWeight():
	gender,age,height,weight,act_level = personData()
	bmr = getBMR(gender,age,height,weight,act_level)
	
	bmr = (bmr*.8)
	print("\nYou need to consume: "+str(bmr)+" calroies per day in order to roughly lose 1lb of fat per week.")
	back = input("Press ENTER to return...\n")


def gainWeight():
	gender,age,height,weight,act_level = personData()
	bmr = getBMR(gender,age,height,weight,act_level)
	
	bmr = (bmr*1.2)
	print("\nYou need to consume: "+str(bmr)+" calroies per day in order to gain muscle.")
	back = input("Press ENTER to return...\n")
	
def sel():
	choice = input()	
	
	if(choice == '1'):
		printBMR()	
	if(choice == '2'):
		loseWeight()
	if(choice == '3'):
		gainWeight()
# MAIN	
while(1):	
	print_menu()	
	sel()	

