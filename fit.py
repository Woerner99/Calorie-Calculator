"""
Calorie Calculator 

Author: Sean-Michael Woerner
Date: 02/04/2021

"""
#====================================================================
#Imports:
#====================================================================
import os


#====================================================================
#Globals:
#====================================================================
save = 0


#====================================================================
# Subroutines
#====================================================================
def print_menu():
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print("*******************************************")
	print("*	  Calorie Calculator              *")
	print("*                                         *")
	print("*        by: Sean-Michael Woerner         *")
	print("*******************************************")
	print("\nMain Menu\n---------")
	print("(1) Calculate BMR")
	print("(2) Calculate Calories Needed to Lose Weight")
	print("(3) Calculate Calroies Needed to Gain Weight")
	print("(4) Erase Profiles")
	print("---------------------------------------------")

#This method uses the Harris-Benedict Formula
def getBMR(gender, age, height, weight, bfp, act_level):

	#Calculate Lean Mass (this will be used to calculate BMR)
	weight = weight*(1-bfp)

	#Male
	if(gender==1):
		bmr = 66.47 + (6.24*weight) + (12.7*height) - (6.755*age)
	#Female
	if(gender==2):
		bmr = 655.1 + (4.35*weight) + (4.7*height) - (4.7*age)

	return (float(bmr*act_level))
# Print the BMR to the screen
def printBMR():
	gender,age,height,weight,bfp,act_level = personData()
	bmr = getBMR(gender,age,height,weight,bfp,act_level)

	print("\nYour Calculated BMR is: "+str(bmr)+" calories burned per day.")
	doWeSave(bmr)
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

	bmr = (bmr*.8)
	print("\nYou need to consume: "+str(bmr)+" calroies per day in order to roughly lose 1lb of fat per week.")
	doWeSave(bmr)
	back = input("Press ENTER to return...\n")

# Calculate BMR to gain weight
def gainWeight():
	gender,age,height,weight,bfp,act_level = personData()
	bmr = getBMR(gender,age,height,weight,bfp,act_level)

	bmr = (bmr*1.2)
	print("\nYou need to consume: "+str(bmr)+" calroies per day in order to gain muscle.")
	doWeSave(bmr)
	back = input("Press ENTER to return...\n")

# Boolean function to determine whether or not to save the profile of user
# 1 means save, else do nothing
def doWeSave(bmr):
	save = int(input("Would you like to save this entry?\n(1) YES\n(2) NO\n"))
	if (save == 1):
		name = input("Enter your name: ")
		saveProfile(name, bmr)
		print("Profile has been saved as user: " + name)

# Save portfolio of to text file, writes person's name and BMR
def saveProfile(name, bmr):
	f = open("profiles.txt","a")
	f.write(name+" "+str(bmr)+"\n")
	f.close()
# Erases profiles.txt if it exists in the project folder
def eraseProfiles():
	if os.path.exists("profiles.txt"):
		os.remove("profiles.txt")
	else:
		print("There are no profiles saved...")
		back = input("Press ENTER to return...\n")

# Menu selection entered by user
def sel():
	choice = input()

	if(choice == '1'):
		printBMR()
	if(choice == '2'):
		loseWeight()
	if(choice == '3'):
		gainWeight()
	if(choice == '4'):
		eraseProfiles()
#====================================================================
# Main
#====================================================================

while(1):	
	print_menu()	
	sel()	

