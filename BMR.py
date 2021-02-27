#====================================================================
# bmr.py
# author: Sean-Michael Woerner

# contains all BMR related functions
#====================================================================

#====================================================================
#Imports:
#====================================================================
import os
import Profile


#====================================================================
# Subroutines
#====================================================================
#This method uses the Harris-Benedict Formula
def getBMR(gender, age, height, weight, bfp, act_level):

	#Calculate Lean Mass (this will be used to calculate BMR)
	leanMass = weight*(1-bfp)

	#Male
	if(gender==1):
		bmr = 66.47 + (6.24*leanMass) + (12.7*height) - (6.755*age)
	#Female
	if(gender==2):
		bmr = 655.1 + (4.35*leanMass) + (4.7*height) - (4.7*age)

	return (float(bmr*act_level))


def printBMR():
	gender,age,height,weight,bfp,act_level = personData()
	bmr = getBMR(gender,age,height,weight,bfp,act_level)

	print("\nYour Calculated BMR is: "+str(bmr)+" calories burned per day.")
	Profile.doWeSave(bmr)
	back = input("Press ENTER to return...\n")


# Gets users data and can be used to calculate BMR
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
	bfp = float(input("What is your body fat percentage? (For 20% = 0.2) \n"))
	act_level = float(input("What is your activity level?\n(1.2) Sedentary\n(1.375) 1-3 days of exercise per week\n(1.55)"
							" 3-5 days of exercise per week\n(1.725) 6-7 days of exercise per week\n(1.9) Very hard exercise daily\n"
							"(x) Or enter a custom activity level\n"))


	return gender,age,height,weight,bfp,act_level

# Calculate BMR to lose weight
def loseWeight():
	gender,age,height,weight,bfp,act_level = personData()
	bmr = getBMR(gender,age,height,weight,bfp,act_level)

	bmrLose = (bmr*.8)
	print("\nYou need to consume: "+str(bmrLose)+" calroies per day in order to roughly lose 1lb of fat per week.")
	Profile.doWeSave(bmr)
	back = input("Press ENTER to return...\n")

# Calculate BMR to gain weight
def gainWeight():
	gender,age,height,weight,bfp,act_level = personData()
	bmr = getBMR(gender,age,height,weight,bfp,act_level)

	bmrGain = (bmr*1.2)
	print("\nYou need to consume: "+str(bmrGain)+" calroies per day in order to gain muscle.")
	Profile.doWeSave(bmr)
	back = input("Press ENTER to return...\n")