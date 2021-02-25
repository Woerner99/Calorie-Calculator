"""
Calorie Calculator 

Author: Sean-Michael Woerner
Date: 02/04/2021

"""
#====================================================================
#Imports:
#====================================================================
import os
import BMR
import Profile

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
	print("*	       Calorie Calculator             *")
	print("*                                         *")
	print("*        by: Sean-Michael Woerner         *")
	print("*******************************************")
	print("\nMain Menu\n---------")
	print("(1) Calculate BMR")
	print("(2) Calculate Calories Needed to Lose Weight")
	print("(3) Calculate Calroies Needed to Gain Weight")
	print("(4) Erase Profiles")
	print("---------------------------------------------")

# Menu selection entered by user
def sel():
	choice = input()
	if(choice == '1'):
		BMR.printBMR()
	if(choice == '2'):
		BMR.loseWeight()
	if(choice == '3'):
		BMR.gainWeight()
	if(choice == '4'):
		Profile.eraseProfiles()

#====================================================================
# Main
#====================================================================
while(1):	
	print_menu()	
	sel()	

